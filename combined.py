from openai import OpenAI
import numpy as np
import faiss
import googlemaps
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import logging
from urllib.parse import urljoin
from dotenv import load_dotenv
import re

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
YELP_API_KEY = os.getenv('YELP_API_KEY')

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of user agents for rotation
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    # Add more user agents
]

# MongoDB meals database
# connecting to the MongoDB instance and retrieving the meal data
# Query the database and generating recommendations 

'''
from tinydb import TinyDB
import logging

try:
    # Connect to TinyDB by opening (or creating) the JSON file
    db = TinyDB('glo_eat_app.json')
    meals_table = db.table('meals')
    
    logging.info("Successfully connected to TinyDB")
    
    # Retrieve all meal documents from the 'meals' table
    meal_docs = meals_table.all()
    print("Fetched", len(meal_docs), "meals")
    
except Exception as e:
    logging.error(f"Failed to connect to TinyDB: {e}")
    meal_docs = []
    
finally:
    db.close()
'''
import json
import logging

try:
    with open('glo_eat_app.json', 'r') as f:
        data = json.load(f)
    # Extract meals from the dictionary values
    meal_docs = list(data.get("meals", {}).values())
    logging.info("Successfully loaded meals manually from JSON")
    print("Fetched", len(meal_docs), "meals")
except Exception as e:
    logging.error(f"Error loading meals manually: {e}")
    meal_docs = []


""" ========== GENERATE EMBEDDINGS ========== """
# Generate embeddings with text-embedding-3-small
def get_embedding(text):
    response = client.embeddings.create(input=text, model="text-embedding-3-small")
    return np.array(response.data[0].embedding, dtype=np.float32)

meal_texts = [f"{meal['name']} {meal['description']} {' '.join(meal['typical_ingredients'])}" for meal in meal_docs]
meal_embeddings = np.array([get_embedding(text) for text in meal_texts])

# FAISS index
dim = meal_embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(meal_embeddings)





""" ========== DIETARY JSON FILTERING FUNCTION ========== """

dietary_json = {    
    "vegan": {
        "exclude": ["meat", "fish", "dairy", "eggs", "honey", "gelatin", "minced meat", "beef", "pork", "chicken", "turkey", "lamb", "goat", "bacon", "sausage", "ham", "salami", "pepperoni", "seafood", "meats", "rabbit", "goat", "mutton", "beef heart", "meat stock", "salmon", "tuna", "cod", "halibut", "trout", "cod","bass", "tilapia", "catfish", "mackerel", "sardine", "anchovy", "clownfish", "pufferfish", "seabass", "seabream", "stingray", "hilsa fish", "hilsa", "mixed seafood", "dried fish", "raw fish", "salted fish", "salted cod", "whitebait", "hemingway", "haddock", "conger eel", "eel"],
        "include": ["vegetables", "fruits", "nuts", "seeds", "legumes", "beans", "lentils", "peas", "chickpeas", "lentil", "pea", "chickpea", "lupin", "tofu"]
    },
      "gluten_intolerance": {
        "exclude": ["wheat", "barley", "rye", "bread", "cake", "pasta", "beer", "cereal", "bun", "pita bread", "rye bread", "flatbread", "breadcrumbs", "oats", "oatmeal", "dough", "phyllo dough", "flour"]
      },
      "lactose_intolerance": {
        "exclude": ["milk", "cheese", "butter", "cream", "yoghurt", "ghee", "ghee butter", "raclette cheese", "condensed milk", "kefir"]
      },
      "dairy_allergy": {
        "exclude": ["milk", "cheese", "butter", "cream", "mayonnaise", "sour cream", "yogurt", "ice cream", "cream cheese", "whipped cream", "margarine", "mascarpone", "ricotta", "mozzarella", "cheddar", "parmesan", "salami", "cow milk", "mayo", "ghee", "ghee butter", "yoghurt", "raclette cheese", "condensed milk", "kefir"]
      },
      "egg_allergy": {
        "exclude": ["egg", "egg yolk", "egg white", "mayonnaise", "margarine", "mascarpone", "boiled egg", "fried egg", "scrambled egg", "poached egg", "hard boiled egg", "soft boiled egg"]
      },
      "peanut_allergy": {
        "exclude": ["peanut", "peanut butter", "peanuts"]
      },
      "shellfish_allergy": {
        "exclude": ["shellfish", "crab", "lobster", "shrimp", "crustacean", "crayfish", "prawns", "king prawns"]
      },
      "mollusk_allergy": {
        "exclude": ["mollusk", "mussels", "scallops", "squid", "octopus", "oyster", "clams", "abalone", "oysters", "snails", "prawns", "king prawns"]
      },
      "fish_allergy": {
        "exclude": ["fish", "salmon", "tuna", "cod", "halibut", "trout", "cod","bass", "tilapia", "catfish", "mackerel", "sardine", "anchovy", "clownfish", "pufferfish", "seabass", "seabream", "stingray", "hilsa fish", "hilsa", "mixed seafood", "dried fish", "raw fish", "salted fish", "salted cod", "whitebait", "hemingway", "haddock", "conger eel", "eel" ]
      },
      "soy_allergy": {
        "exclude": ["soy", "soy sauce", "soybean", "soybean oil", "soybean flour", "soybean meal"]
      },
      "legume_allergy": {
        "exclude": ["legume", "legumes", "beans", "lentils", "peas", "chickpeas", "lentil", "pea", "chickpea", "lupin", "black beans", "pinto beans", "kidney beans", "black eyed peas"]
      },
      "nut_allergy": {
        "exclude": ["almonds", "walnuts", "peanuts", "hazelnuts", "pecans", "cashews", "brazil nuts", "pistachios", "macadamia nuts", "pine nuts", "chestnuts", "pecan", "cashew", "brazil nut", "pistachio", "macadamia nut", "pine nut", "chestnut"]
      },
      "pescetarian": {
        "exclude": ["meat", "beef", "pork", "chicken", "turkey", "lamb", "goat", "bacon", "sausage", "ham", "salami", "pepperoni", "minced meat", "dried meat", "salted meat", "rabbit", "goat", "mutton"],
        "include": ["fish", "seafood"]
      },
      "vegetarian": {
        "exclude": ["ground meat", "meat", "fish", "beef", "pork", "chicken", "turkey", "lamb", "goat", "bacon", "sausage", "ham", "salami", "pepperoni", "seafood", "meats", "minced meat", "dried meat", "salted meat", "rabbit", "goat", "mutton", "chorizo", "bacon", "beef heart", "meat stock", "salmon", "tuna", "cod", "halibut", "trout", "cod","bass", "tilapia", "catfish", "mackerel", "sardine", "anchovy", "clownfish", "pufferfish", "seabass", "seabream", "stingray", "hilsa fish", "hilsa", "mixed seafood", "dried fish", "raw fish", "salted fish", "salted cod", "whitebait", "hemingway", "haddock", "conger eel", "eel"],
        "include": ["dairy", "eggs"]
      },
      "ketogenic": {
        "exclude": ["bread", "pasta", "potatoes", "rice", "sugar", "dairy"],
        "requirements": {"fat": "high", "carb": "low"}
      },
      "paleo": {
        "exclude": ["dairy", "sugar", "dairy", "grains", "legumes", "sweetener", "trans fats", "artificial sweeteners", "vegetable oil"],
        "include": ["meat", "fruits", "vegetables", "nuts"]
      },
      "kosher": {
        "exclude": ["pork", "sausage", "ham", "poultry","shellfish"],
        "include": ["kosher meat", "kosher dairy"]
      },
      "halal": {
        "exclude": ["pork", "poultry","shellfish", "alcohol", "beer", "white wine", "red wine"],
        "include": ["halal meat"]
      }
 } # your dietary rules here


def dietary_filter(meal, user_restrictions):
    ingredients = " ".join(meal.get("typical_ingredients", [])).lower()
    for restriction in user_restrictions:
        excludes = dietary_json[restriction]["exclude"]
        if any(ing.lower() in ingredients for ing in excludes):
            return False
    return True



""" ========== SCRAPING MENU FUNCTIONS ========== """

def extract_menu_links_from_google_data(place):
    """Extract menu links from Google Places data."""
    menu_links = []
    editorial_summary = place.get("editorialSummary", {}).get("text", "")
    if "menu" in editorial_summary.lower():
        # Extract potential menu links from the summary
        menu_links.extend(re.findall(r'https?://[^\s]+', editorial_summary))
    
    # Check photos for menu links
    for photo in place.get("photos", []):
        if "menu" in photo.get("name", "").lower():
            menu_links.append(photo.get("url", ""))
    
    return menu_links

def scrape_website(url):
    """Scrape a website for menu links using Selenium and BeautifulSoup."""
    try:
        # Configure Selenium
        options = Options()
        options.add_argument('--headless')
        options.add_argument(f'user-agent={random.choice(USER_AGENTS)}')
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        
        # Parse the page
        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()
        
        # Extract menu links or content
        menu_links = []
        for a in soup.select('a[href]'):
            link_text = a.get_text(separator=" ").strip().lower()
            link_url = a['href'].lower()
            if "menu" in link_text or "menu" in link_url:
                menu_links.append(urljoin(url, a['href']))
        
        return menu_links
    except Exception as e:
        logging.error(f"Error scraping {url}: {e}")
        return []

def fetch_menu_from_yelp(restaurant_name, location):
    """Fetch menu data from Yelp Fusion API."""
    if not YELP_API_KEY:
        logging.warning("Yelp API key not found. Skipping Yelp API.")
        return {}
    
    headers = {"Authorization": f"Bearer {YELP_API_KEY}"}
    params = {
        "term": restaurant_name,
        "location": location,
        "limit": 1
    }
    response = requests.get("https://api.yelp.com/v3/businesses/search", headers=headers, params=params)
    response.raise_for_status()
    businesses = response.json().get("businesses", [])
    
    if not businesses:
        return {}
    
    business_id = businesses[0].get("id", "")
    menu_response = requests.get(f"https://api.yelp.com/v3/businesses/{business_id}", headers=headers)
    return menu_response.json().get("menu", {})

def scrape_menu_page(url):
    """Scrape a menu page using Selenium."""
    try:
        # Configure Selenium
        options = Options()
        options.add_argument('--headless')
        options.add_argument(f'user-agent={random.choice(USER_AGENTS)}')
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        
        # Wait for the page to load (adjust timeout as needed)
        driver.implicitly_wait(10)
        
        # Extract the page source
        page_source = driver.page_source
        driver.quit()
        
        return page_source
    except Exception as e:
        logging.error(f"Error scraping {url} with Selenium: {e}")
        return None

def extract_menu_text(html):
    """Extract menu text from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    
    # Remove scripts and styles
    for tag in soup(["script", "style"]):
        tag.decompose()
    
    # Extract text
    return " ".join(soup.stripped_strings)

def parse_menu_with_gpt(menu_text):
    """Parse menu text using OpenAI GPT."""
    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API key missing.")
    
    try:
        # Use GPT-3.5-turbo as the default model
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Updated to GPT-3.5-turbo
            messages=[
                {"role": "system", "content": "You are a helpful assistant that extracts structured data from restaurant menus."},
                {"role": "user", "content": f"""
                The following is a restaurant menu. Extract the dish names, descriptions, and prices in JSON format:
                
                {menu_text}
                
                Example output:
                {{
                  "menu": [
                    {{
                      "dish": "Chicken Ruby",
                      "description": "A rich and creamy chicken curry.",
                      "price": "£12.50"
                    }},
                    {{
                      "dish": "Garlic Naan",
                      "description": "Freshly baked naan with garlic butter.",
                      "price": "£3.00"
                    }}
                  ]
                }}
                """}
            ]
        )
        
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error parsing menu with GPT: {e}")
        return {}



""" ========== GET RESTAURANT MENU FUNCTION ========== """
def get_restaurant_menu(place):
    """Get the menu for a restaurant using all available methods."""
    restaurant_name = place.get("displayName", {}).get("text", "Unknown Restaurant")
    website = place.get("websiteUri", "")
    location = place.get("formattedAddress", "")
    
    # Step 1: Check Google Places data for menu links
    menu_links = extract_menu_links_from_google_data(place)
    
    # Step 2: Scrape the restaurant's website for menu links
    if not menu_links and website:
        menu_links = scrape_website(website)
    
    # Step 3: Use Yelp API to fetch menu data
    menu_data = {}
    if not menu_links:
        menu_data = fetch_menu_from_yelp(restaurant_name, location)
    
    # Step 4: Scrape menu pages and extract text
    menu_text = ""
    for link in menu_links:
        try:
            html = scrape_menu_page(link)
            if html:
                menu_text += extract_menu_text(html) + "\n"
        except Exception as e:
            logging.error(f"Error scraping menu page {link}: {e}")
    
    # Step 5: Parse menu text with GPT
    if menu_text:
        return parse_menu_with_gpt(menu_text)
    elif menu_data:
        return menu_data
    else:
        return {}

# Search and recommendation function
def recommend_restaurants(query, user_location, user_restrictions, radius=2000):
    query_embedding = get_embedding(query)
    _, indices = index.search(np.array([query_embedding]), k=10)
    candidate_meals = [meal_docs[i] for i in indices[0]]

    # Dietary filtering
    verified_meals = [meal for meal in candidate_meals if dietary_filter(meal, user_restrictions)]
    if not verified_meals:
        return []

    # Dynamic restaurant search via Google Maps API
    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)
    restaurants = gmaps.places_nearby(location=user_location, radius=radius, type="restaurant")

    recommendations = []
    for rest in restaurants.get("results", []):
        menu = get_restaurant_menu(rest)  # Use the scraping function
        for meal in verified_meals:
            meal_name = meal["name"].lower()
            if meal_name in menu.lower():
                recommendations.append({
                    "restaurant": rest["name"],
                    "address": rest["vicinity"],
                    "meal": meal["name"],
                    "description": meal["description"],
                })
    return recommendations

# Example use:
results = recommend_restaurants(
    query="vegan lasagna",
    user_location=(51.5074, -0.1278),  # London
    user_restrictions=["vegan"],
    radius=500
)

for res in results:
    print(res["restaurant"], "serves", res["meal"])