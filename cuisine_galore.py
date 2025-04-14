from tinydb import TinyDB, Query


#from pymongo import MongoClient
#from pymongo.errors import ConnectionFailure

# Connect to MongoDB (adjust the connection string as needed)
#client = MongoClient('mongodb://localhost:5500/')
#db = client['glo_eat_app']
#meals_collection = db['meals']

# Define sample meal documents grouped by cuisine

meals = [
# United States
     {
    "name": "Hamburger",
    "cuisine": "American",
    "meal_type": "Main Course",
    "category": "Fast Food",
    "typical_ingredients": ["beef patty", "bun", "lettuce", "tomato", "cheese", "pickles"],
    "description": "A classic American sandwich with a grilled beef patty and various toppings.",
    "tags": ["grilled", "fast food", "comfort food"]
},

     {
    "name": "BBQ Ribs",
    "cuisine": "American",
    "meal_type": "Main Course",
    "category": "Grilled Meat",
    "typical_ingredients": ["pork ribs", "BBQ sauce", "spices", "brown sugar"],
    "description": "Slow-cooked pork ribs coated in a tangy and sweet BBQ sauce.",
    "tags": ["smoky", "sweet", "grilled"]
},

 {
    "name": "Apple Pie",
    "cuisine": "American",
    "meal_type": "Dessert",
    "category": "Pastry",
    "typical_ingredients": ["apples", "sugar", "cinnamon", "pastry crust"],
    "description": "A classic American dessert made with spiced apples baked in a flaky crust.",
    "tags": ["sweet", "baked", "comfort food"]
},

# Chinese
{
    "name": "Sweet and Sour Pork",
    "cuisine": "Chinese",
    "meal_type": "Main Course",
    "category": "Pork Dish",
    "typical_ingredients": ["pork", "pineapple", "bell peppers", "vinegar", "sugar"],
    "description": "A classic Chinese dish with crispy pork and a tangy sweet and sour sauce.",
    "tags": ["tangy", "crispy", "stir-fry"]
},

 {
    "name": "Peking Duck",
    "cuisine": "Chinese",
    "meal_type": "Main Course",
    "category": "Duck Dish",
    "typical_ingredients": ["duck", "hoisin sauce", "pancakes", "scallions"],
    "description": "A famous Chinese dish featuring crispy roasted duck served with pancakes and sauce.",
    "tags": ["crispy", "savory", "festive"]
},

{
    "name": "Dim Sum",
    "cuisine": "Chinese",
    "meal_type": "Appetizer",
    "category": "Dumplings",
    "typical_ingredients": ["shrimp", "pork", "wrappers", "ginger", "soy sauce"],
    "description": "A variety of small Chinese dishes, including dumplings and buns, often served in bamboo steamers.",
    "tags": ["steamed", "savory", "bite-sized"]
},


# India 
 {
    "name": "Butter Chicken",
    "cuisine": "Indian",
    "meal_type": "Main Course",
    "category": "Chicken Dish",
    "typical_ingredients": ["chicken", "tomato", "cream", "butter", "spices"],
    "description": "A rich and creamy Indian curry made with tender chicken and aromatic spices.",
    "tags": ["creamy", "spicy", "comfort food"]
},

{
    "name": "Biryani",
    "cuisine": "Indian",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["rice", "chicken", "spices", "yogurt", "saffron"],
    "description": "A fragrant Indian rice dish layered with spiced meat and cooked to perfection.",
    "tags": ["aromatic", "spicy", "festive"]
},

{
    "name": "Samosas",
    "cuisine": "Indian",
    "meal_type": "Appetizer",
    "category": "Fried Snack",
    "typical_ingredients": ["potatoes", "peas", "spices", "pastry", "oil"],
    "description": "Crispy fried pastries filled with spiced potatoes and peas.",
    "tags": ["crispy", "spicy", "snack"]
},


# Japanese 
 {
    "name": "Sushi",
    "cuisine": "Japanese",
    "meal_type": "Main Course",
    "category": "Seafood Dish",
    "typical_ingredients": ["rice", "fish", "seaweed", "vinegar", "soy sauce"],
    "description": "A traditional Japanese dish of vinegared rice paired with raw fish or other seafood.",
    "tags": ["fresh", "raw", "delicate"]
},

 {
    "name": "Ramen",
    "cuisine": "Japanese",
    "meal_type": "Main Course",
    "category": "Noodle Soup",
    "typical_ingredients": ["noodles", "broth", "pork", "eggs", "scallions"],
    "description": "A Japanese noodle soup with rich broth, toppings, and chewy noodles.",
    "tags": ["hearty", "savory", "comfort food"]
},

 {
    "name": "Tempura",
    "cuisine": "Japanese",
    "meal_type": "Appetizer",
    "category": "Fried Dish",
    "typical_ingredients": ["shrimp", "vegetables", "batter", "oil", "flour"],
    "description": "Lightly battered and deep-fried seafood or vegetables.",
    "tags": ["crispy", "light", "fried"]
},

#France 
 {
    "name": "Coq au Vin",
    "cuisine": "French",
    "meal_type": "Main Course",
    "category": "Chicken Dish",
    "typical_ingredients": ["chicken", "red wine", "bacon", "mushrooms", "onions"],
    "description": "A French classic of chicken braised in red wine with mushrooms and onions.",
    "tags": ["braised", "rich", "comfort food"]
},

 {
    "name": "Croissant",
    "cuisine": "French",
    "meal_type": "Breakfast",
    "category": "Pastry",
    "typical_ingredients": ["butter", "flour", "yeast", "milk"],
    "description": "A flaky and buttery French pastry, often enjoyed for breakfast.",
    "tags": ["flaky", "buttery", "breakfast"]
},

{
    "name": "Ratatouille",
    "cuisine": "French",
    "meal_type": "Main Course",
    "category": "Vegetable Dish",
    "typical_ingredients": ["eggplant", "zucchini", "tomatoes", "bell peppers", "herbs"],
    "description": "A Provençal vegetable stew made with fresh summer vegetables.",
    "tags": ["vegetarian", "aromatic", "comfort food"]
},



#Italy 
{
    "name": "Spaghetti Carbonara",
    "cuisine": "Italian",
    "meal_type": "Main Course",
    "category": "Pasta Dish",
    "typical_ingredients": ["spaghetti", "eggs", "Parmesan cheese", "pancetta", "black pepper"],
    "description": "A creamy Italian pasta dish made with eggs, cheese, and pancetta.",
    "tags": ["creamy", "savory", "comfort food"]
},

{
    "name": "Pizza Margherita",
    "cuisine": "Italian",
    "meal_type": "Main Course",
    "category": "Pizza",
    "typical_ingredients": ["tomato sauce", "mozzarella", "basil", "olive oil"],
    "description": "A classic Italian pizza with tomato, mozzarella, and fresh basil.",
    "tags": ["cheesy", "simple", "comfort food"]
},

{
    "name": "Tiramisu",
    "cuisine": "Italian",
    "meal_type": "Dessert",
    "category": "Cake",
    "typical_ingredients": ["ladyfingers", "coffee", "mascarpone", "cocoa powder", "dairy", "eggs"],
    "description": "A creamy Italian dessert made with coffee-soaked ladyfingers and mascarpone.",
    "tags": ["creamy", "coffee", "dessert"]
},


# Mexican
 {
    "name": "Tacos al Pastor",
    "cuisine": "Mexican",
    "meal_type": "Main Course",
    "category": "Pork Dish",
    "typical_ingredients": ["pork", "pineapple", "corn tortillas", "onions", "cilantro"],
    "description": "A Mexican street food favorite with marinated pork and pineapple on corn tortillas.",
    "tags": ["spicy", "grilled", "street food"]
},

{
    "name": "Mole Poblano",
    "cuisine": "Mexican",
    "meal_type": "Main Course",
    "category": "Sauce Dish",
    "typical_ingredients": ["chicken", "chocolate", "chilies", "spices", "sesame seeds"],
    "description": "A rich and complex Mexican sauce made with chocolate and chilies, served over chicken.",
    "tags": ["spicy", "sweet", "festive"]
},
 {
    "name": "Churros",
    "cuisine": "Mexican",
    "meal_type": "Dessert",
    "category": "Fried Pastry",
    "typical_ingredients": ["flour", "sugar", "cinnamon", "oil", "chocolate sauce"],
    "description": "Fried dough pastry dusted with sugar and cinnamon, often served with chocolate sauce.",
    "tags": ["sweet", "crispy", "dessert"]
},



#British 
 {
    "name": "Fish and Chips",
    "cuisine": "British",
    "meal_type": "Main Course",
    "category": "Seafood Dish",
    "typical_ingredients": ["fish", "potatoes", "batter", "salt", "vinegar"],
    "description": "A British classic of deep-fried fish served with crispy fries.",
    "tags": ["fried", "comfort food", "seafood"]
},

 {
    "name": "Full English Breakfast",
    "cuisine": "British",
    "meal_type": "Breakfast",
    "category": "Breakfast Dish",
    "typical_ingredients": ["eggs", "bacon", "sausages", "beans", "tomatoes", "toast"],
    "description": "A hearty British breakfast featuring eggs, bacon, sausages, and more.",
    "tags": ["hearty", "savory", "breakfast"]
},

 {
    "name": "Shepherd's Pie",
    "cuisine": "British",
    "meal_type": "Main Course",
    "category": "Casserole",
    "typical_ingredients": ["lamb", "potatoes", "vegetables", "gravy"],
    "description": "A comforting casserole of ground lamb and vegetables topped with mashed potatoes.",
    "tags": ["hearty", "baked", "comfort food"]
},


#Brazilian
 {
    "name": "Feijoada",
    "cuisine": "Brazilian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["black beans", "pork", "sausage", "beef", "onions"],
    "description": "A hearty Brazilian stew made with black beans and various meats.",
    "tags": ["hearty", "slow-cooked", "comfort food"]
},

 {
    "name": "Pão de Queijo",
    "cuisine": "Brazilian",
    "meal_type": "Snack",
    "category": "Bread",
    "typical_ingredients": ["tapioca flour", "cheese", "eggs", "milk"],
    "description": "Cheesy and chewy Brazilian bread rolls made with tapioca flour.",
    "tags": ["cheesy", "gluten-free", "snack"]
},

 {
    "name": "Brigadeiro",
    "cuisine": "Brazilian",
    "meal_type": "Dessert",
    "category": "Candy",
    "typical_ingredients": ["condensed milk", "cocoa powder", "butter", "chocolate sprinkles"],
    "description": "A Brazilian chocolate truffle made with condensed milk and cocoa.",
    "tags": ["sweet", "chocolate", "dessert"]
},

#Thai

 {
    "name": "Pad Thai",
    "cuisine": "Thai",
    "meal_type": "Main Course",
    "category": "Noodle Dish",
    "typical_ingredients": ["rice noodles", "shrimp", "tofu", "eggs", "peanuts"],
    "description": "A popular Thai stir-fried noodle dish with a balance of sweet, sour, and savory flavors.",
    "tags": ["stir-fry", "tangy", "nutty"]
},

 {
    "name": "Tom Yum Goong",
    "cuisine": "Thai",
    "meal_type": "Soup",
    "category": "Seafood Soup",
    "typical_ingredients": ["shrimp", "lemongrass", "chilies", "lime leaves", "mushrooms"],
    "description": "A spicy and sour Thai soup made with shrimp and aromatic herbs.",
    "tags": ["spicy", "sour", "aromatic"]
},

 {
    "name": "Green Curry",
    "cuisine": "Thai",
    "meal_type": "Main Course",
    "category": "Curry",
    "typical_ingredients": ["green curry paste", "coconut milk", "chicken", "eggplant", "basil"],
    "description": "A creamy and spicy Thai curry made with green curry paste and coconut milk.",
    "tags": ["spicy", "creamy", "aromatic"]
},


#Spanish

 {
    "name": "Paella",
    "cuisine": "Spanish",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["rice", "saffron", "seafood", "chicken", "bell peppers"],
    "description": "A traditional Spanish rice dish cooked with saffron and a variety of meats or seafood.",
    "tags": ["aromatic", "savory", "festive"]
},

 {
    "name": "Gazpacho",
    "cuisine": "Spanish",
    "meal_type": "Appetizer",
    "category": "Cold Soup",
    "typical_ingredients": ["tomatoes", "cucumbers", "bell peppers", "garlic", "olive oil"],
    "description": "A refreshing cold soup made with fresh vegetables, perfect for summer.",
    "tags": ["cold", "refreshing", "vegetarian"]
},

 {
    "name": "Churros con Chocolate",
    "cuisine": "Spanish",
    "meal_type": "Dessert",
    "category": "Fried Pastry",
    "typical_ingredients": ["flour", "sugar", "cinnamon", "oil", "chocolate sauce"],
    "description": "Fried dough pastry served with thick hot chocolate for dipping.",
    "tags": ["sweet", "crispy", "dessert"]
},

#German

 {
    "name": "Bratwurst",
    "cuisine": "German",
    "meal_type": "Main Course",
    "category": "Sausage Dish",
    "typical_ingredients": ["sausage", "mustard", "bread", "sauerkraut", "pork"],
    "description": "A German sausage dish often served with mustard and sauerkraut.",
    "tags": ["grilled", "savory", "street food"]
},

 {
    "name": "Schnitzel",
    "cuisine": "German",
    "meal_type": "Main Course",
    "category": "Fried Meat",
    "typical_ingredients": ["pork", "veal", "bread", "eggs", "lemon"],
    "description": "A thin, breaded, and fried cutlet of meat, often served with lemon.",
    "tags": ["crispy", "savory", "comfort food"]
},

 {
    "name": "Black Forest Cake",
    "cuisine": "German",
    "meal_type": "Dessert",
    "category": "Cake",
    "typical_ingredients": ["cake", "cherries", "whipped cream", "kirsch", "dairy", "sugar", "eggs"],
    "description": "A decadent German cake made with chocolate, cherries, and whipped cream.",
    "tags": ["sweet", "chocolate", "festive"]
},

#Canadian

 {
    "name": "Poutine",
    "cuisine": "Canadian",
    "meal_type": "Main Course",
    "category": "Comfort Food",
    "typical_ingredients": ["fries", "cheese curds", "gravy", "potatoes", "cheese", "dairy"],
    "description": "A Canadian comfort food of fries topped with cheese curds and gravy.",
    "tags": ["cheesy", "comfort food", "savory"]
},

 {
    "name": "Butter Tarts",
    "cuisine": "Canadian",
    "meal_type": "Dessert",
    "category": "Pastry",
    "typical_ingredients": ["butter", "sugar", "eggs", "pastry crust", "raisins", "dairy"],
    "description": "A sweet Canadian pastry filled with a gooey butter-sugar mixture.",
    "tags": ["sweet", "gooey", "dessert"]
},

{
    "name": "Nanaimo Bars",
    "cuisine": "Canadian",
    "meal_type": "Dessert",
    "category": "Candy",
    "typical_ingredients": ["chocolate", "custard", "coconut", "butter", "dairy", "eggs"],
    "description": "A no-bake Canadian dessert bar with layers of chocolate, custard, and coconut.",
    "tags": ["sweet", "chocolate", "dessert"]
},



#Australian

 {
    "name": "Meat Pie",
    "cuisine": "Australian",
    "meal_type": "Main Course",
    "category": "Pastry Dish",
    "typical_ingredients": ["beef", "pastry", "gravy", "onions", "flour", "minced meat"],
    "description": "A savory Australian pie filled with minced meat and gravy.",
    "tags": ["savory", "comfort food", "pastry"]
},

 {
    "name": "Pavlova",
    "cuisine": "Australian",
    "meal_type": "Dessert",
    "category": "Meringue",
    "typical_ingredients": ["egg whites", "sugar", "cream", "fruit"],
    "description": "A light and airy meringue dessert topped with whipped cream and fresh fruit.",
    "tags": ["sweet", "light", "festive"]
},

 {
    "name": "Vegemite on Toast",
    "cuisine": "Australian",
    "meal_type": "Breakfast",
    "category": "Spread",
    "typical_ingredients": ["Vegemite", "bread", "butter"],
    "description": "A classic Australian breakfast of toast spread with Vegemite, a salty yeast extract.",
    "tags": ["salty", "simple", "breakfast"]
},


#South Korean 

{
    "name": "Bibimbap",
    "cuisine": "Korean",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["rice", "vegetables", "beef", "egg", "gochujang"],
    "description": "A Korean mixed rice dish with vegetables, meat, and a spicy sauce.",
    "tags": ["spicy", "colorful", "balanced"]
},

 {
    "name": "Kimchi",
    "cuisine": "Korean",
    "meal_type": "Side Dish",
    "category": "Fermented Dish",
    "typical_ingredients": ["napa cabbage", "radish", "chili powder", "garlic", "ginger"],
    "description": "A spicy and tangy fermented vegetable dish, often served as a side.",
    "tags": ["spicy", "fermented", "tangy"]
},

{
    "name": "Korean BBQ",
    "cuisine": "Korean",
    "meal_type": "Main Course",
    "category": "Grilled Meat",
    "typical_ingredients": ["beef", "pork", "soy sauce", "garlic", "sesame oil"],
    "description": "A Korean dining experience where diners grill their own meat at the table.",
    "tags": ["grilled", "savory", "interactive"]
},

#Greek
 {
    "name": "Moussaka",
    "cuisine": "Greek",
    "meal_type": "Main Course",
    "category": "Casserole",
    "typical_ingredients": ["eggplant", "meat", "tomatoes", "béchamel sauce"],
    "description": "A Greek casserole made with layers of eggplant, ground meat, and béchamel sauce.",
    "tags": ["baked", "hearty", "comfort food"]
},

 {
    "name": "Souvlaki",
    "cuisine": "Greek",
    "meal_type": "Main Course",
    "category": "Grilled Meat",
    "typical_ingredients": ["pork", "olive oil", "lemon", "oregano", "pita bread"],
    "description": "Grilled meat skewers, often served with pita bread and tzatziki.",
    "tags": ["grilled", "savory", "street food"]
},

{
    "name": "Baklava",
    "cuisine": "Greek",
    "meal_type": "Dessert",
    "category": "Pastry",
    "typical_ingredients": ["phyllo dough", "nuts", "honey", "butter"],
    "description": "A sweet pastry made with layers of phyllo dough, nuts, and honey syrup.",
    "tags": ["sweet", "nutty", "dessert"]
},

#Turkish 

 {
    "name": "Kebab",
    "cuisine": "Turkish",
    "meal_type": "Main Course",
    "category": "Grilled Meat",
    "typical_ingredients": ["lamb", "yogurt", "spices", "flatbread", "bread"],
    "description": "A Turkish dish of grilled meat, often served with yogurt and flatbread.",
    "tags": ["grilled", "savory", "spiced"]
},

{
    "name": "Baklava",
    "cuisine": "Turkish",
    "meal_type": "Dessert",
    "category": "Pastry",
    "typical_ingredients": ["phyllo dough", "nuts", "honey", "butter", "dough"],
    "description": "A sweet pastry made with layers of phyllo dough, nuts, and honey syrup.",
    "tags": ["sweet", "nutty", "dessert"]
},

 {
    "name": "Meze",
    "cuisine": "Turkish",
    "meal_type": "Appetizer",
    "category": "Small Plates",
    "typical_ingredients": ["chickpeas", "tzatziki", "dolma", "eggplant", "olives"],
    "description": "A selection of small dishes served as appetizers or snacks.",
    "tags": ["varied", "flavorful", "shared"]
},


# Carribbean 

{
    "name": "Jerk Chicken",
    "cuisine": "Caribbean",
    "meal_type": "Main Course",
    "category": "Grilled Meat",
    "typical_ingredients": ["chicken", "Scotch bonnet peppers", "allspice", "thyme", "garlic"],
    "description": "A spicy and smoky Caribbean dish of grilled chicken marinated in jerk seasoning.",
    "tags": ["spicy", "grilled", "aromatic"]
},

 {
    "name": "Roti",
    "cuisine": "Caribbean",
    "meal_type": "Main Course",
    "category": "Flatbread",
    "typical_ingredients": ["flour", "curried meat", "potatoes", "chickpeas"],
    "description": "A Caribbean flatbread filled with curried meat and vegetables.",
    "tags": ["spicy", "hearty", "comfort food"]
},

 {
    "name": "Callaloo",
    "cuisine": "Caribbean",
    "meal_type": "Side Dish",
    "category": "Vegetable Dish",
    "typical_ingredients": ["callaloo leaves", "okra", "coconut milk", "crab"],
    "description": "A Caribbean green stew made with leafy vegetables and coconut milk.",
    "tags": ["creamy", "hearty", "vegetarian"]
},

# Ghanaian
 {
    "name": "Waakye",
    "cuisine": "Ghanaian",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["rice", "beans", "sorghum leaves", "spices"],
    "description": "A Ghanaian dish of rice and beans cooked with sorghum leaves for a unique color and flavor.",
    "tags": ["hearty", "nutritious", "comfort food"]
},

 {
    "name": "Banku and Tilapia",
    "cuisine": "Ghanaian",
    "meal_type": "Main Course",
    "category": "Seafood Dish",
    "typical_ingredients": ["corn", "dough", "tilapia", "peppers", "onions", "fish"],
    "description": "A traditional Ghanaian dish of fermented corn dough served with grilled tilapia.",
    "tags": ["fermented", "grilled", "savory"]
},

 {
    "name": "Kelewele",
    "cuisine": "Ghanaian",
    "meal_type": "Snack",
    "category": "Fried Dish",
    "typical_ingredients": ["plantains", "ginger", "chilies", "spices"],
    "description": "Spicy fried plantains, often served as a snack or side dish.",
    "tags": ["spicy", "sweet", "fried"]
},

#Moroccan

 {
    "name": "Tagine",
    "cuisine": "Moroccan",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["lamb", "apricots", "almonds", "spices", "couscous"],
    "description": "A slow-cooked Moroccan stew made with meat, fruits, and spices.",
    "tags": ["aromatic", "slow-cooked", "sweet and savory"]
},

 {
    "name": "Couscous",
    "cuisine": "Moroccan",
    "meal_type": "Main Course",
    "category": "Grain Dish",
    "typical_ingredients": ["couscous", "vegetables", "meat", "spices"],
    "description": "A staple Moroccan dish of steamed couscous served with vegetables and meat.",
    "tags": ["steamed", "hearty", "comfort food"]
},

 {
    "name": "Harira",
    "cuisine": "Moroccan",
    "meal_type": "Soup",
    "category": "Lentil Soup",
    "typical_ingredients": ["lentils", "tomatoes", "chickpeas", "lamb", "spices"],
    "description": "A hearty Moroccan soup often served during Ramadan.",
    "tags": ["spicy", "hearty", "comfort food"]
},

#Egyptian

 {
    "name": "Koshari",
    "cuisine": "Egyptian",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["rice", "lentils", "pasta", "tomato sauce", "onions"],
    "description": "A popular Egyptian street food made with rice, lentils, pasta, and a spicy tomato sauce.",
    "tags": ["hearty", "spicy", "comfort food"]
},

 {
    "name": "Ful Medames",
    "cuisine": "Egyptian",
    "meal_type": "Breakfast",
    "category": "Bean Dish",
    "typical_ingredients": ["fava beans", "garlic", "lemon", "olive oil", "cumin", "beans"],
    "description": "A traditional Egyptian breakfast of mashed fava beans, often served with bread.",
    "tags": ["hearty", "savory", "breakfast"]
},

 {
    "name": "Molokhia",
    "cuisine": "Egyptian",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["molokhia leaves", "chicken", "garlic", "coriander", "rice"],
    "description": "A green leafy soup made with molokhia leaves, often served with rice or bread.",
    "tags": ["earthy", "hearty", "comfort food"]
},


#Ethiopian

{
    "name": "Koshari",
    "cuisine": "Egyptian",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["rice", "lentils", "pasta", "tomato sauce", "fried onions"],
    "description": "A popular Egyptian street food made with rice, lentils, pasta, and a spicy tomato sauce.",
    "tags": ["hearty", "spicy", "comfort food"]
},

 {
    "name": "Ful Medames",
    "cuisine": "Egyptian",
    "meal_type": "Breakfast",
    "category": "Bean Dish",
    "typical_ingredients": ["fava beans", "garlic", "lemon", "olive oil", "cumin", "beans"],
    "description": "A traditional Egyptian breakfast of mashed fava beans, often served with bread.",
    "tags": ["hearty", "savory", "breakfast"]
},

 {
    "name": "Molokhia",
    "cuisine": "Egyptian",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["molokhia leaves", "chicken", "garlic", "coriander", "rice"],
    "description": "A green leafy soup made with molokhia leaves, often served with rice or bread.",
    "tags": ["earthy", "hearty", "comfort food"]
},

#Iranian

 {
    "name": "Chelow Kabab",
    "cuisine": "Iranian",
    "meal_type": "Main Course",
    "category": "Grilled Meat",
    "typical_ingredients": ["rice", "lamb", "saffron", "butter", "grilled tomatoes", "onions"],
    "description": "A Persian dish of saffron rice served with grilled meat and tomatoes.",
    "tags": ["grilled", "aromatic", "festive"]
},

 {
    "name": "Ghormeh Sabzi",
    "cuisine": "Iranian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["herbs", "lamb", "kidney beans", "dried lime", "rice", "onions"],
    "description": "A fragrant Persian herb stew made with lamb and served with rice.",
    "tags": ["aromatic", "hearty", "comfort food"]
},

 {
    "name": "Tahdig",
    "cuisine": "Iranian",
    "meal_type": "Side Dish",
    "category": "Rice Dish",
    "typical_ingredients": ["rice", "yogurt", "saffron", "butter", "dairy"],
    "description": "The crispy, golden crust of Persian rice, often served as a side.",
    "tags": ["crispy", "savory", "comfort food"]
},

#Lebanese
 {
    "name": "Falafel",
    "cuisine": "Lebanese",
    "meal_type": "Main Course",
    "category": "Vegetarian Dish",
    "typical_ingredients": ["chickpeas", "herbs", "spices", "sesame seeds", "pita bread"],
    "description": "Deep-fried balls made from ground chickpeas and herbs, often served in pita bread.",
    "tags": ["vegetarian", "crispy", "street food"]
},

 {
    "name": "Tabbouleh",
    "cuisine": "Lebanese",
    "meal_type": "Side Dish",
    "category": "Salad",
    "typical_ingredients": ["parsley", "bulgur", "tomatoes", "lemon", "olive oil", "wheat"],
    "description": "A refreshing Lebanese salad made with parsley, bulgur, and fresh vegetables.",
    "tags": ["fresh", "light", "vegetarian"]
},


 {
    "name": "Shawarma",
    "cuisine": "Lebanese",
    "meal_type": "Main Course",
    "category": "Grilled Meat",
    "typical_ingredients": ["chicken", "garlic sauce", "pickles", "pita bread", "spices"],
    "description": "Grilled meat wrapped in pita bread, often served with garlic sauce and pickles.",
    "tags": ["grilled", "savory", "street food"]
},

#Vietnamese
{
    "name": "Pho",
    "cuisine": "Vietnamese",
    "meal_type": "Main Course",
    "category": "Noodle Soup",
    "typical_ingredients": ["rice noodles", "beef", "broth", "herbs", "bean sprouts"],
    "description": "A Vietnamese noodle soup with fragrant broth, rice noodles, and herbs.",
    "tags": ["aromatic", "hearty", "comfort food"]
},

 {
    "name": "Banh Mi",
    "cuisine": "Vietnamese",
    "meal_type": "Main Course",
    "category": "Sandwich",
    "typical_ingredients": ["bread", "pork", "pickled vegetables", "cilantro", "chili"],
    "description": "A Vietnamese sandwich filled with meat, pickled vegetables, and herbs.",
    "tags": ["crunchy", "savory", "street food"]
},

 {
    "name": "Goi Cuon",
    "cuisine": "Vietnamese",
    "meal_type": "Appetizer",
    "category": "Spring Rolls",
    "typical_ingredients": ["rice paper", "shrimp", "pork", "herbs", "noodles"],
    "description": "Fresh spring rolls filled with shrimp, pork, and herbs, served with dipping sauce.",
    "tags": ["fresh", "light", "refreshing"]
},

#Philippian
 {
    "name": "Adobo",
    "cuisine": "Filipino",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["chicken", "soy sauce", "vinegar", "garlic", "bay leaves"],
    "description": "A Filipino stew of meat marinated in soy sauce, vinegar, and garlic.",
    "tags": ["tangy", "savory", "comfort food"]
},

 {
    "name": "Sinigang",
    "cuisine": "Filipino",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["tamarind", "pork", "vegetables", "fish"],
    "description": "A sour Filipino soup made with tamarind and various meats or seafood.",
    "tags": ["sour", "hearty", "comfort food"]
},

 {
    "name": "Halo-Halo",
    "cuisine": "Filipino",
    "meal_type": "Dessert",
    "category": "Shaved Ice",
    "typical_ingredients": ["shaved ice", "sweet beans", "fruit", "leche flan", "ube ice cream", "evaporated milk", "dairy", "ube"],
    "description": "A colorful Filipino dessert made with shaved ice, sweet toppings, and evaporated milk.",
    "tags": ["sweet", "refreshing", "dessert"]
},

#Nigerian 

 {
    "name": "Jollof Rice",
    "cuisine": "Nigerian",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["rice", "tomatoes", "onions", "peppers", "spices", "vegetable oil"],
    "description": "A flavorful one-pot rice dish cooked with tomatoes, peppers, and spices, often served at celebrations.",
    "tags": ["spicy", "aromatic", "festive"]
},

 {
    "name": "Pounded Yam and Egusi Soup",
    "cuisine": "Nigerian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["yam", "egusi seeds", "spinach", "palm oil", "meat", "stockfish", "seeds"],
    "description": "A hearty Nigerian dish of pounded yam served with a rich melon seed soup, often accompanied by meat or fish.",
    "tags": ["hearty", "nutritious", "comfort food"]
},


 {
    "name": "Suya",
    "cuisine": "Nigerian",
    "meal_type": "Snack",
    "category": "Grilled Meat",
    "typical_ingredients": ["beef", "peanuts", "spices", "oil", "onions"],
    "description": "Spicy grilled meat skewers, often served with sliced onions and sometimes with a side of fresh tomatoes.",
    "tags": ["spicy", "grilled", "street food"]
},

{
    "name": "Moin Moin",
    "cuisine": "Nigerian",
    "meal_type": "Side Dish",
    "category": "Steamed Pudding",
    "typical_ingredients": ["black-eyed peas", "peppers", "onions", "vegetable oil", "fish", "eggs"],
    "description": "A steamed bean pudding made from blended black-eyed peas, often served as a side or snack.",
    "tags": ["steamed", "protein-rich", "vegetarian"]
},

 {
    "name": "Akara",
    "cuisine": "Nigerian",
    "meal_type": "Breakfast",
    "category": "Fried Snack",
    "typical_ingredients": ["black-eyed peas", "onions", "peppers", "oil"],
    "description": "Deep-fried bean cakes made from blended black-eyed peas, often served with bread or pap (ogi).",
    "tags": ["crispy", "protein-rich", "breakfast"]
},

 {
    "name": "Efo Riro",
    "cuisine": "Nigerian",
    "meal_type": "Main Course",
    "category": "Vegetable Stew",
    "typical_ingredients": ["spinach", "peppers", "tomatoes", "palm oil", "meat or fish"],
    "description": "A rich and spicy vegetable stew, often served with pounded yam, eba, or rice.",
    "tags": ["spicy", "hearty", "vegetarian-friendly"]
},

 {
    "name": "Ofada Rice and Ayamase Stew",
    "cuisine": "Nigerian",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["ofada rice", "green peppers", "red peppers", "palm oil", "assorted meat", "rice"],
    "description": "A local Nigerian dish of unpolished rice served with a spicy green pepper stew.",
    "tags": ["spicy", "aromatic", "festive"]
},

 {
    "name": "Pepper Soup",
    "cuisine": "Nigerian",
    "meal_type": "Soup",
    "category": "Spicy Soup",
    "typical_ingredients": ["goat", "fish", "peppers", "utazi leaves", "spices"],
    "description": "A spicy and aromatic soup often served as a starter or remedy for colds.",
    "tags": ["spicy", "aromatic", "comfort food"]
},

 {
    "name": "Amala and Ewedu Soup",
    "cuisine": "Nigerian",
    "meal_type": "Main Course",
    "category": "Swallow Dish",
    "typical_ingredients": ["yam flour", "ewedu leaves", "okra", "stockfish", "meat"],
    "description": "A traditional Yoruba dish of yam flour served with a slimy soup made from jute leaves.",
    "tags": ["slimy", "hearty", "comfort food"]
},

 {
    "name": "Banga Soup",
    "cuisine": "Nigerian",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["palm fruit extract", "meat", "fish", "spices", "starch"],
    "description": "A rich and flavorful soup made from palm fruit extract, often served with starch or fufu.",
    "tags": ["rich", "aromatic", "hearty"]
},

 {
    "name": "Puff Puff",
    "cuisine": "Nigerian",
    "meal_type": "Snack",
    "category": "Fried Dough",
    "typical_ingredients": ["flour", "sugar", "yeast", "oil"],
    "description": "A popular Nigerian snack of deep-fried dough balls, often enjoyed at parties or as a street food.",
    "tags": ["sweet", "fried", "snack"]
},

 {
    "name": "Chin Chin",
    "cuisine": "Nigerian",
    "meal_type": "Snack",
    "category": "Fried Snack",
    "typical_ingredients": ["flour", "sugar", "butter", "milk", "oil"],
    "description": "A crunchy fried snack made from dough, often enjoyed with tea or as a dessert.",
    "tags": ["crunchy", "sweet", "snack"]
},

 {
    "name": "Oha Soup",
    "cuisine": "Nigerian",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["oha leaves", "cocoyam", "palm oil", "meat", "stockfish"],
    "description": "A traditional Igbo soup made with oha leaves, often served with fufu or eba.",
    "tags": ["aromatic", "hearty", "comfort food"]
},

 {
    "name": "Nigerian Fried Rice",
    "cuisine": "Nigerian",
    "meal_type": "Main Course",
    "category": "Fried Rice",
    "typical_ingredients": ["rice", "vegetables", "carrots", "peas", "green beans", "bell peppers", "onions", "tomato paste", "curry powder", "thyme", "chicken", "shrimp"],
    "description": "A vibrant and aromatic Nigerian fried rice, enriched with colorful vegetables, a blend of spices, and your choice of protein, perfect for festive gatherings.",
    "tags": ["spicy", "colorful", "stir-fried"]
},


# Indonesian

 {
    "name": "Nasi Goreng",
    "cuisine": "Indonesian",
    "meal_type": "Main Course",
    "category": "Fried Rice",
    "typical_ingredients": ["rice", "egg", "chicken", "shrimp", "spices"],
    "description": "A flavorful Indonesian fried rice dish with a mix of spices and often topped with a fried egg.",
    "tags": ["spicy", "fragrant", "street food"]
},
 {
    "name": "Rendang",
    "cuisine": "Indonesian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["beef", "coconut milk", "lemongrass", "galangal", "spices"],
    "description": "A rich, slow-cooked beef stew simmered in coconut milk and spices.",
    "tags": ["spicy", "hearty", "traditional"]
},
 {
    "name": "Satay",
    "cuisine": "Indonesian",
    "meal_type": "Main Course",
    "category": "Grilled Dish",
    "typical_ingredients": ["meat", "peanut sauce", "lemongrass", "skewers"],
    "description": "Grilled skewers of marinated meat served with a savory peanut sauce.",
    "tags": ["grilled", "savory", "skewered"]
},
 {
    "name": "Gado-Gado",
    "cuisine": "Indonesian",
    "meal_type": "Main Course",
    "category": "Salad",
    "typical_ingredients": ["vegetables", "tofu", "tempeh", "peanut sauce", "soybeans"],
    "description": "A vibrant vegetable salad drizzled with a spicy peanut dressing.",
    "tags": ["fresh", "colorful", "vegetarian"]
},
 {
    "name": "Soto Ayam",
    "cuisine": "Indonesian",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["chicken", "turmeric", "lemongrass", "noodles", "vegetables"],
    "description": "A comforting chicken soup infused with turmeric and aromatic herbs.",
    "tags": ["hearty", "aromatic", "light"]
},
 {
    "name": "Bakso",
    "cuisine": "Indonesian",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["meatballs", "noodles", "broth", "green onions"],
    "description": "A savory meatball soup often enjoyed as a filling meal.",
    "tags": ["comforting", "savory", "noodle soup"]
},
 {
    "name": "Gudeg",
    "cuisine": "Indonesian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["jackfruit", "coconut milk", "spices", "eggs"],
    "description": "A sweet and savory stew made from young jackfruit simmered in coconut milk.",
    "tags": ["sweet", "rich", "traditional"]
},
 {
    "name": "Ikan Bakar",
    "cuisine": "Indonesian",
    "meal_type": "Main Course",
    "category": "Grilled Fish",
    "typical_ingredients": ["fish", "spices", "lime", "herbs"],
    "description": "Grilled fish marinated with a blend of spices and citrus for a smoky flavor.",
    "tags": ["grilled", "smoky", "zesty"]
},
 {
    "name": "Pempek",
    "cuisine": "Indonesian",
    "meal_type": "Main Course",
    "category": "Fish Cake",
    "typical_ingredients": ["fish", "tapioca", "vinegar", "spices"],
    "description": "Savory fish cakes made from ground fish and tapioca, served with a tangy sauce.",
    "tags": ["unique", "chewy", "flavored"]
},
 {
    "name": "Mie Goreng",
    "cuisine": "Indonesian",
    "meal_type": "Main Course",
    "category": "Noodle Dish",
    "typical_ingredients": ["noodles", "vegetables", "egg", "soy sauce", "spices"],
    "description": "Stir-fried noodles tossed with vegetables and a savory sauce.",
    "tags": ["stir-fried", "savory", "quick"]
},

#Malaysian
 {
    "name": "Nasi Lemak",
    "cuisine": "Malaysian",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["coconut milk rice", "sambal", "anchovies", "egg", "peanuts"],
    "description": "Fragrant coconut rice served with spicy sambal, anchovies, boiled egg, and peanuts.",
    "tags": ["aromatic", "spicy", "traditional"]
},
 {
    "name": "Laksa",
    "cuisine": "Malaysian",
    "meal_type": "Main Course",
    "category": "Noodle Soup",
    "typical_ingredients": ["noodles", "coconut milk", "shrimp", "spices", "herbs"],
    "description": "A rich and spicy noodle soup with a creamy coconut broth.",
    "tags": ["spicy", "creamy", "noodle soup"]
},
 {
    "name": "Char Kway Teow",
    "cuisine": "Malaysian",
    "meal_type": "Main Course",
    "category": "Stir-fried Noodles",
    "typical_ingredients": ["rice noodles", "shrimp", "sausage", "bean sprouts", "soy sauce"],
    "description": "Stir-fried flat rice noodles with shrimp, sausage, and a smoky soy sauce flavor.",
    "tags": ["stir-fried", "smoky", "savory"]
},
 {
    "name": "Roti Canai",
    "cuisine": "Malaysian",
    "meal_type": "Side Dish",
    "category": "Flatbread",
    "typical_ingredients": ["flour", "water", "oil", "salt"],
    "description": "Flaky and crispy flatbread often served with a side of curry.",
    "tags": ["crispy", "flaky", "versatile"]
},
 {
    "name": "Satay",
    "cuisine": "Malaysian",
    "meal_type": "Main Course",
    "category": "Grilled Skewers",
    "typical_ingredients": ["chicken or beef", "spices", "peanut sauce", "lemongrass"],
    "description": "Grilled skewered meat served with a rich and savory peanut sauce.",
    "tags": ["grilled", "savory", "skewered"]
},
 {
    "name": "Hainanese Chicken Rice",
    "cuisine": "Malaysian",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["chicken", "fragrant rice", "ginger", "garlic", "chili sauce"],
    "description": "Poached chicken served with aromatic rice and a flavorful dipping sauce.",
    "tags": ["tender", "fragrant", "simple"]
},
 {
    "name": "Nasi Kerabu",
    "cuisine": "Malaysian",
    "meal_type": "Main Course",
    "category": "Colored Rice Dish",
    "typical_ingredients": ["blue rice", "herbs", "vegetables", "fish"],
    "description": "Vibrantly colored rice mixed with fresh herbs and served with assorted sides.",
    "tags": ["colorful", "herbal", "unique"]
},
 {
    "name": "Mee Rebus",
    "cuisine": "Malaysian",
    "meal_type": "Main Course",
    "category": "Noodle Dish",
    "typical_ingredients": ["noodles", "thick gravy", "potato", "egg", "spices"],
    "description": "Noodles served in a thick, slightly sweet and spicy gravy.",
    "tags": ["hearty", "rich", "comforting"]
},
 {
    "name": "Assam Pedas",
    "cuisine": "Malaysian",
    "meal_type": "Main Course",
    "category": "Fish Stew",
    "typical_ingredients": ["fish", "tamarind", "chili", "spices", "herbs"],
    "description": "A tangy and spicy fish stew flavored with tamarind and chili.",
    "tags": ["tangy", "spicy", "sour"]
},
 {
    "name": "Curry Laksa",
    "cuisine": "Malaysian",
    "meal_type": "Main Course",
    "category": "Curry Noodle Soup",
    "typical_ingredients": ["noodles", "coconut milk", "curry spices", "seafood or chicken"],
    "description": "A spicy, coconut-curry noodle soup enriched with seafood or chicken.",
    "tags": ["creamy", "spicy", "rich"]
},

#Singaporean
 {
    "name": "Hainanese Chicken Rice",
    "cuisine": "Singaporean",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["chicken", "fragrant rice", "ginger", "chili", "cucumber"],
    "description": "Tender poached chicken served with aromatic rice and chili sauce.",
    "tags": ["flavorful", "simple", "iconic"]
},
 {
    "name": "Chilli Crab",
    "cuisine": "Singaporean",
    "meal_type": "Main Course",
    "category": "Seafood Dish",
    "typical_ingredients": ["crab", "tomato", "chili", "garlic", "egg"],
    "description": "Fresh crab cooked in a tangy, spicy tomato-based sauce.",
    "tags": ["spicy", "messy", "finger-licking"]
},
 {
    "name": "Laksa",
    "cuisine": "Singaporean",
    "meal_type": "Main Course",
    "category": "Noodle Soup",
    "typical_ingredients": ["rice noodles", "coconut milk", "shrimp", "spices"],
    "description": "A creamy, spicy noodle soup with Peranakan influences.",
    "tags": ["creamy", "spicy", "rich"]
},
 {
    "name": "Satay",
    "cuisine": "Singaporean",
    "meal_type": "Main Course",
    "category": "Grilled Skewers",
    "typical_ingredients": ["meat", "peanut sauce", "lemongrass", "spices"],
    "description": "Skewered and grilled marinated meat served with a savory peanut sauce.",
    "tags": ["grilled", "savory", "skewered"]
},
 {
    "name": "Char Kway Teow",
    "cuisine": "Singaporean",
    "meal_type": "Main Course",
    "category": "Stir-fried Noodle Dish",
    "typical_ingredients": ["rice noodles", "seafood", "bean sprouts", "soy sauce", "egg"],
    "description": "Stir-fried flat rice noodles with seafood and a smoky sauce.",
    "tags": ["stir-fried", "smoky", "savory"]
},
 {
    "name": "Hokkien Mee",
    "cuisine": "Singaporean",
    "meal_type": "Main Course",
    "category": "Noodle Dish",
    "typical_ingredients": ["yellow noodles", "prawns", "pork", "broth", "soy sauce"],
    "description": "Stir-fried noodles in a rich prawn and pork broth.",
    "tags": ["savory", "hearty", "noodle dish"]
},
 {
    "name": "Kaya Toast",
    "cuisine": "Singaporean",
    "meal_type": "Breakfast",
    "category": "Breakfast Dish",
    "typical_ingredients": ["toast", "coconut jam", "butter"],
    "description": "Toasted bread spread with sweet coconut jam, typically enjoyed for breakfast.",
    "tags": ["sweet", "crispy", "simple"]
},
 {
    "name": "Bak Kut Teh",
    "cuisine": "Singaporean",
    "meal_type": "Main Course",
    "category": "Herbal Pork Soup",
    "typical_ingredients": ["pork ribs", "herbs", "garlic", "soy sauce", "spices"],
    "description": "A comforting pork rib soup simmered with a blend of traditional herbs.",
    "tags": ["herbal", "rich", "savory"]
},
 {
    "name": "Sambal Stingray",
    "cuisine": "Singaporean",
    "meal_type": "Main Course",
    "category": "Grilled Seafood",
    "typical_ingredients": ["stingray", "sambal", "lime", "herbs"],
    "description": "Grilled stingray drizzled with a spicy sambal sauce.",
    "tags": ["spicy", "grilled", "zesty"]
},
 {
    "name": "Rojak",
    "cuisine": "Singaporean",
    "meal_type": "Appetizer",
    "category": "Salad",
    "typical_ingredients": ["fruits", "vegetables", "tofu", "peanut sauce", "spices"],
    "description": "A tangy and sweet salad of mixed fruits and vegetables tossed in a spicy sauce.",
    "tags": ["refreshing", "tangy", "sweet"]
},

#Pakistani
 {
    "name": "Biryani",
    "cuisine": "Pakistani",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["basmati rice", "meat", "spices", "yogurt", "saffron"],
    "description": "A fragrant rice dish layered with marinated meat and aromatic spices.",
    "tags": ["spicy", "aromatic", "rich"]
},
 {
    "name": "Nihari",
    "cuisine": "Pakistani",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["beef", "bone marrow", "spices", "ginger", "garlic"],
    "description": "A slow-cooked beef stew enjoyed as a hearty breakfast.",
    "tags": ["rich", "spicy", "comforting"]
},
 {
    "name": "Haleem",
    "cuisine": "Pakistani",
    "meal_type": "Main Course",
    "category": "Porridge/Stew",
    "typical_ingredients": ["meat", "lentils", "wheat", "spices", "ghee"],
    "description": "A thick, hearty stew made with meat, lentils, and wheat, slow-cooked to perfection.",
    "tags": ["hearty", "nutritious", "slow-cooked"]
},
 {
    "name": "Chapli Kebab",
    "cuisine": "Pakistani",
    "meal_type": "Main Course",
    "category": "Grilled Patty",
    "typical_ingredients": ["minced meat", "spices", "herbs", "onions"],
    "description": "A spiced, flattened meat patty that is grilled to perfection.",
    "tags": ["spicy", "grilled", "flavorful"]
},
{
    "name": "Karahi",
    "cuisine": "Pakistani",
    "meal_type": "Main Course",
    "category": "Stir-fry",
    "typical_ingredients": ["chicken", "mutton", "tomatoes", "spices", "ginger", "garlic"],
    "description": "A spicy stir-fry cooked in a wok-like pan with vibrant flavors.",
    "tags": ["spicy", "wok-cooked", "robust"]
},
 {
    "name": "Seekh Kebabs",
    "cuisine": "Pakistani",
    "meal_type": "Main Course",
    "category": "Grilled Skewers",
    "typical_ingredients": ["minced meat", "spices", "herbs", "skewers"],
    "description": "Skewered and grilled spiced meat, perfect for a hearty meal.",
    "tags": ["grilled", "spiced", "succulent"]
},
 {
    "name": "Saag",
    "cuisine": "Pakistani",
    "meal_type": "Main Course",
    "category": "Vegetable Curry",
    "typical_ingredients": ["spinach", "mustard greens", "spices", "cream"],
    "description": "A creamy, spiced curry made with leafy greens and traditional spices.",
    "tags": ["creamy", "healthy", "savory"]
},
 {
    "name": "Daal Chawal",
    "cuisine": "Pakistani",
    "meal_type": "Main Course",
    "category": "Rice and Lentils",
    "typical_ingredients": ["lentils", "rice", "spices", "ghee", "onions"],
    "description": "A simple and comforting dish of spiced lentils served over rice.",
    "tags": ["simple", "comforting", "hearty"]
},
 {
    "name": "Paya",
    "cuisine": "Pakistani",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["goat trotters", "spices", "herbs", "stock"],
    "description": "A rich, gelatinous stew made from slow-cooked trotters.",
    "tags": ["rich", "hearty", "traditional"]
},
 {
    "name": "Samosas",
    "cuisine": "Pakistani",
    "meal_type": "Appetizer",
    "category": "Appetizer",
    "typical_ingredients": ["flour", "potatoes", "peas", "spices", "meat"],
    "description": "Crispy, deep-fried pastry pockets filled with spiced vegetables or meat.",
    "tags": ["crispy", "spiced", "snack"]
},

#Bangladeshi
 {
    "name": "Bhuna Khichuri",
    "cuisine": "Bangladeshi",
    "meal_type": "Main Course",
    "category": "Rice and Lentils",
    "typical_ingredients": ["rice", "lentils", "meat", "spices", "ghee", "butter"],
    "description": "A spiced rice and lentil dish enriched with tender meat.",
    "tags": ["hearty", "spiced", "comforting"]
},
 {
    "name": "Dhaka-Style Biryani",
    "cuisine": "Bangladeshi",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["basmati rice", "marinated meat", "spices", "yogurt", "saffron"],
    "description": "A fragrant biryani with layers of marinated meat and aromatic spices unique to Dhaka.",
    "tags": ["aromatic", "layered", "rich"]
},
 {
    "name": "Ilish Bhapa",
    "cuisine": "Bangladeshi",
    "meal_type": "Main Course",
    "category": "Steamed Fish",
    "typical_ingredients": ["Hilsa fish", "mustard", "green chilies", "spices"],
    "description": "Steamed Hilsa fish prepared with a pungent mustard and spice sauce.",
    "tags": ["pungent", "steamed", "traditional"]
},
 {
    "name": "Panta Bhat",
    "cuisine": "Bangladeshi",
    "meal_type": "Main Course",
    "category": "Fermented Rice Dish",
    "typical_ingredients": ["fermented rice", "salt", "onions", "chili", "lime"],
    "description": "A traditional fermented rice dish often served with an assortment of sides.",
    "tags": ["fermented", "refreshing", "traditional"]
},
 {
    "name": "Bhorta",
    "cuisine": "Bangladeshi",
    "meal_type": "Side Dish",
    "category": "Mashed Dish",
    "typical_ingredients": ["vegetables or fish", "garlic", "chili", "mustard oil"],
    "description": "Mashed vegetables or fish blended with spices and mustard oil for a robust flavor.",
    "tags": ["spicy", "mashed", "flavorful"]
},
 {
    "name": "Kacchi Biryani",
    "cuisine": "Bangladeshi",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["meat", "rice", "spices", "yogurt", "saffron"],
    "description": "A rich biryani where marinated raw meat is cooked with rice for deep flavor.",
    "tags": ["rich", "aromatic", "layered"]
},
 {
    "name": "Shutki Curry",
    "cuisine": "Bangladeshi",
    "meal_type": "Main Course",
    "category": "Curry",
    "typical_ingredients": ["dried fish", "spices", "onions", "tomatoes", "chilli"],
    "description": "A spicy curry made from dried fish, offering bold and robust flavors.",
    "tags": ["spicy", "robust", "savory"]
},
 {
    "name": "Fuchka",
    "cuisine": "Bangladeshi",
    "meal_type": "Snack",
    "category": "Street Food",
    "typical_ingredients": ["puffed puris", "tamarind water", "spiced mashed potatoes", "chickpeas", "flour"],
    "description": "Crispy puris filled with tangy tamarind water and spiced fillings.",
    "tags": ["tangy", "crispy", "street food"]
},
 {
    "name": "Chingri Malai Curry",
    "cuisine": "Bangladeshi",
    "meal_type": "Main Course",
    "category": "Seafood Curry",
    "typical_ingredients": ["prawns", "coconut milk", "spices", "herbs", "chili"],
    "description": "A creamy, mildly spiced prawn curry enriched with coconut milk.",
    "tags": ["creamy", "mild", "aromatic"]
},
 {
    "name": "Luchi with Curry",
    "cuisine": "Bangladeshi",
    "meal_type": "Main Course",
    "category": "Fried Bread with Curry",
    "typical_ingredients": ["flour", "water", "oil", "salt", "curry"],
    "description": "Deep-fried, puffy flatbread served alongside a flavorful curry.",
    "tags": ["crispy", "fluffy", "savory"]
},

#Russian 
 {
    "name": "Borscht",
    "cuisine": "Russian",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["beetroots", "cabbage", "potatoes", "sour cream", "vegetables"],
    "description": "A vibrant beetroot soup served with a dollop of sour cream.",
    "tags": ["hearty", "tangy", "colorful"]
},
 {
    "name": "Pelmeni",
    "cuisine": "Russian",
    "meal_type": "Main Course",
    "category": "Dumplings",
    "typical_ingredients": ["flour", "meat", "onions", "spices"],
    "description": "Delicate meat-filled dumplings often served with butter or broth.",
    "tags": ["savory", "handmade", "comforting"]
},
 {
    "name": "Beef Stroganoff",
    "cuisine": "Russian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["beef", "mushrooms", "sour cream", "onions", "spices"],
    "description": "Tender beef strips in a creamy mushroom sauce served over noodles.",
    "tags": ["creamy", "rich", "hearty"]
},
 {
    "name": "Blini",
    "cuisine": "Russian",
    "meal_type": "Breakfast",
    "category": "Pancakes",
    "typical_ingredients": ["flour", "milk", "egg", "butter"],
    "description": "Thin, delicate pancakes served with toppings such as sour cream or caviar.",
    "tags": ["light", "versatile", "traditional"]
},
 {
    "name": "Pirozhki",
    "cuisine": "Russian",
    "meal_type": "Snack",
    "category": "Stuffed Pastry",
    "typical_ingredients": ["flour", "meat", "vegetables", "onions", "spices"],
    "description": "Small, baked or fried pastries filled with savory ingredients.",
    "tags": ["savory", "handheld", "crispy"]
},
  {
    "name": "Shchi",
    "cuisine": "Russian",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["cabbage", "meat", "vegetables", "spices"],
    "description": "A traditional cabbage soup rich in flavor and comfort.",
    "tags": ["hearty", "warm", "traditional"]
},
  {
    "name": "Solyanka",
    "cuisine": "Russian",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["meat", "pickles", "olives", "tomatoes", "spices"],
    "description": "A tangy and spicy soup made with a medley of meats and pickled ingredients.",
    "tags": ["tangy", "spicy", "complex"]
},
 {
    "name": "Okroshka",
    "cuisine": "Russian",
    "meal_type": "Appetizer",
    "category": "Cold Soup",
    "typical_ingredients": ["vegetables", "kefir", "herbs", "boiled eggs"],
    "description": "A refreshing cold soup combining vegetables and kefir, perfect for summer.",
    "tags": ["refreshing", "light", "cold"]
},
 {
    "name": "Kholodets",
    "cuisine": "Russian",
    "meal_type": "Main Course",
    "category": "Aspic",
    "typical_ingredients": ["meat", "gelatin", "spices", "herbs"],
    "description": "A savory meat jelly served chilled, traditionally enjoyed in winter.",
    "tags": ["gelatinous", "rich", "traditional"]
},
 {
    "name": "Kulebyaka",
    "cuisine": "Russian",
    "meal_type": "Main Course",
    "category": "Layered Pie",
    "typical_ingredients": ["meat", "fish", "mushrooms", "dough", "spices"],
    "description": "A complex layered pie filled with a mix of meats, fish, or mushrooms.",
    "tags": ["savory", "hearty", "artisanal"]
},

#Portuguese
 {
    "name": "Bacalhau à Brás",
    "cuisine": "Portuguese",
    "meal_type": "Main Course",
    "category": "Fish Dish",
    "typical_ingredients": ["cod", "eggs", "potatoes", "onions", "olives"],
    "description": "Shredded salted cod combined with eggs and potatoes in a flavorful dish.",
    "tags": ["savory", "traditional", "hearty"]
},
{
    "name": "Caldo Verde",
    "cuisine": "Portuguese",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["kale", "potatoes", "chorizo", "onions", "garlic"],
    "description": "A comforting kale and potato soup enriched with slices of chorizo.",
    "tags": ["comforting", "hearty", "traditional"]
},
 {
    "name": "Francesinha",
    "cuisine": "Portuguese",
    "meal_type": "Main Course",
    "category": "Sandwich",
    "typical_ingredients": ["bread", "steak", "cheese", "ham", "tomato sauce"],
    "description": "A hearty, layered sandwich smothered in a rich, spicy sauce.",
    "tags": ["hearty", "savory", "fusion"]
},
 {
    "name": "Cataplana de Mariscos",
    "cuisine": "Portuguese",
    "meal_type": "Main Course",
    "category": "Seafood Stew",
    "typical_ingredients": ["seafood", "tomatoes", "garlic", "spices", "herbs"],
    "description": "A seafood stew cooked in a traditional copper cataplana, bursting with flavors.",
    "tags": ["seafood", "flavorful", "traditional"]
},
 {
    "name": "Arroz de Marisco",
    "cuisine": "Portuguese",
    "meal_type": "Main Course",
    "category": "Seafood Rice",
    "typical_ingredients": ["rice", "seafood", "tomatoes", "saffron", "herbs"],
    "description": "A sumptuous rice dish loaded with a variety of fresh seafood.",
    "tags": ["seafood", "aromatic", "rich"]
},
 {
    "name": "Piri-Piri Chicken",
    "cuisine": "Portuguese",
    "meal_type": "Main Course",
    "category": "Grilled Chicken",
    "typical_ingredients": ["chicken", "piri-piri sauce", "garlic", "lemon", "spices"],
    "description": "Spicy grilled chicken marinated in a fiery piri-piri sauce.",
    "tags": ["spicy", "grilled", "zesty"]
},
 {
    "name": "Cozido à Portuguesa",
    "cuisine": "Portuguese",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["meats", "vegetables", "beans", "potatoes", "spices"],
    "description": "A robust stew featuring a medley of meats and vegetables, a Portuguese classic.",
    "tags": ["hearty", "traditional", "stew"]
},
 {
    "name": "Pastéis de Bacalhau",
    "cuisine": "Portuguese",
    "meal_type": "Appetizer",
    "category": "Fritters",
    "typical_ingredients": ["cod", "potatoes", "herbs", "flour", "spices"],
    "description": "Crispy codfish fritters seasoned with herbs and spices.",
    "tags": ["crispy", "savory", "traditional"]
},
 {
    "name": "Polvo à Lagareiro",
    "cuisine": "Portuguese",
    "meal_type": "Main Course",
    "category": "Grilled Octopus",
    "typical_ingredients": ["octopus", "olive oil", "garlic", "potatoes", "herbs"],
    "description": "Roasted octopus drizzled with olive oil and garlic, served with potatoes.",
    "tags": ["grilled", "aromatic", "seafood"]
},
 {
    "name": "Pastel de Nata",
    "cuisine": "Portuguese",
    "meal_type": "Dessert",
    "category": "Dessert",
    "typical_ingredients": ["flour", "custard", "sugar", "cinnamon"],
    "description": "A flaky custard tart with a caramelized top, a beloved Portuguese dessert.",
    "tags": ["sweet", "creamy", "iconic"]
},

#Hungarian
 {
    "name": "Goulash",
    "cuisine": "Hungarian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["beef", "paprika", "onions", "tomatoes", "caraway"],
    "description": "A hearty beef stew flavored with generous amounts of paprika.",
    "tags": ["hearty", "spicy", "traditional"]
},
 {
    "name": "Chicken Paprikash",
    "cuisine": "Hungarian",
    "meal_type": "Main Course",
    "category": "Chicken Dish",
    "typical_ingredients": ["chicken", "paprika", "sour cream", "onions", "garlic"],
    "description": "Tender chicken simmered in a creamy paprika sauce.",
    "tags": ["creamy", "spicy", "comforting"]
},
 {
    "name": "Lángos",
    "cuisine": "Hungarian",
    "meal_type": "Snack",
    "category": "Fried Bread",
    "typical_ingredients": ["flour", "yeast", "oil", "garlic", "sour cream"],
    "description": "Deep-fried dough often topped with garlic, cheese, or sour cream.",
    "tags": ["crispy", "fluffy", "savory"]
},
 {
    "name": "Pörkölt",
    "cuisine": "Hungarian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["meat", "paprika", "onions", "tomatoes", "spices"],
    "description": "A rich meat stew simmered with paprika and vegetables.",
    "tags": ["rich", "hearty", "spicy"]
},
 {
    "name": "Hortobágyi Palacsinta",
    "cuisine": "Hungarian",
    "meal_type": "Main Course",
    "category": "Stuffed Crepes",
    "typical_ingredients": ["crepes", "minced meat", "paprika sauce", "onions", "dairy", "flour", "eggs"],
    "description": "Savory crepes filled with a spiced meat mixture in a paprika sauce.",
    "tags": ["creamy", "savory", "traditional"]
},
  {   "name": "Halászlé",
    "cuisine": "Hungarian",
    "meal_type": "Main Course",
    "category": "Fish Soup",
    "typical_ingredients": ["fish", "paprika", "tomatoes", "onions", "spices"],
    "description": "A fiery fishermans soup brimming with river fish and paprika.",
    "tags": ["spicy", "hearty", "traditional"]
  },
 {
    "name": "Töltött Káposzta",
    "cuisine": "Hungarian",
    "meal_type": "Main Course",
    "category": "Stuffed Cabbage Rolls",
    "typical_ingredients": ["cabbage", "minced meat", "rice", "spices", "tomato sauce"],
    "description": "Cabbage leaves stuffed with a flavorful mix of meat and rice.",
    "tags": ["hearty", "comforting", "traditional"]
},
 {
    "name": "Dobos Torte",
    "cuisine": "Hungarian",
    "meal_type": "Dessert",
    "category": "Dessert",
    "typical_ingredients": ["cake", "chocolate buttercream", "caramel", "nuts"],
    "description": "A layered sponge cake with chocolate buttercream and a caramel topping.",
    "tags": ["sweet", "decadent", "layered"]
},
 {
    "name": "Rakott Krumpli",
    "cuisine": "Hungarian",
    "meal_type": "Main Course",
    "category": "Potato Casserole",
    "typical_ingredients": ["potatoes", "eggs", "sausage", "sour cream", "cheese"],
    "description": "A layered casserole of potatoes, eggs, and sausage baked to perfection.",
    "tags": ["hearty", "comforting", "layered"]
},
 {
    "name": "Somlói Galuska",
    "cuisine": "Hungarian",
    "meal_type": "Dessert",
    "category": "Dessert",
    "typical_ingredients": ["cake", "chocolate", "nuts", "cream"],
    "description": "A traditional sponge cake dessert served with chocolate and walnuts.",
    "tags": ["sweet", "rich", "decadent"]
},

#Belgian 
 {
    "name": "Moules-Frites",
    "cuisine": "Belgian",
    "meal_type": "Main Course",
    "category": "Seafood Dish",
    "typical_ingredients": ["mussels", "fries", "butter", "garlic", "parsley", "potatoes"],
    "description": "Fresh mussels steamed in white wine and served with crispy fries.",
    "tags": ["savory", "fresh", "classic"]
},
 {
    "name": "Belgian Waffles",
    "cuisine": "Belgian",
    "meal_type": "Breakfast",
    "category": "Breakfast/Dessert",
    "typical_ingredients": ["flour", "eggs", "milk", "sugar", "butter"],
    "description": "Light and crispy waffles often enjoyed with sweet toppings.",
    "tags": ["crispy", "sweet", "light"]
},
 {
    "name": "Carbonnade Flamande",
    "cuisine": "Belgian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["beef", "beer", "onions", "mustard", "spices"],
    "description": "A slow-cooked beef stew braised in Belgian beer.",
    "tags": ["rich", "hearty", "savory"]
},
 {
    "name": "Waterzooi",
    "cuisine": "Belgian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["chicken", "fish", "vegetables", "cream", "eggs", "herbs"],
    "description": "A creamy stew of chicken or fish with a medley of vegetables.",
    "tags": ["creamy", "comforting", "rich"]
},
 {
    "name": "Stoofvlees",
    "cuisine": "Belgian",
    "meal_type": "Main Course",
    "category": "Beef Stew",
    "typical_ingredients": ["beef", "beer", "onions", "spices", "herbs"],
    "description": "A Flemish beef stew slow-cooked in beer, served with fries.",
    "tags": ["hearty", "rich", "savory"]
},
 {
    "name": "Filet Americain",
    "cuisine": "Belgian",
    "meal_type": "Appetizer",
    "category": "Raw Meat Dish",
    "typical_ingredients": ["beef", "spices", "onions", "capers", "egg yolk"],
    "description": "A seasoned raw beef tartare often enjoyed as a spread.",
    "tags": ["raw", "spiced", "savory"]
},
 {
    "name": "Belgian Endive Gratin",
    "cuisine": "Belgian",
    "meal_type": "Main Course",
    "category": "Gratin",
    "typical_ingredients": ["Belgian endives", "ham", "cheese", "cream", "breadcrumbs"],
    "description": "Baked endives layered with ham and melted cheese in a creamy sauce.",
    "tags": ["creamy", "savory", "baked"]
},
 {
    "name": "Rabbit Stew (Civet de Lapin)",
    "cuisine": "Belgian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["rabbit", "wine", "onions", "herbs", "spices"],
    "description": "A robust rabbit stew simmered with red wine and herbs.",
    "tags": ["hearty", "robust", "savory"]
},
 {
    "name": "Paling in 't Groen",
    "cuisine": "Belgian",
    "meal_type": "Main Course",
    "category": "Fish Dish",
    "typical_ingredients": ["eel", "herbs", "spinach", "cream", "garlic"],
    "description": "Eel cooked in a vibrant green herb sauce.",
    "tags": ["herbal", "unique", "savory"]
},
 {
    "name": "Boudin Noir",
    "cuisine": "Belgian",
    "meal_type": "Main Course",
    "category": "Sausage",
    "typical_ingredients": ["pork blood", "pork", "spices", "onions", "herbs"],
    "description": "A traditional blood sausage with a rich and savory profile.",
    "tags": ["rich", "savory", "traditional"]
},

#Swiss
 {
    "name": "Fondue",
    "cuisine": "Swiss",
    "meal_type": "Main Course",
    "category": "Cheese Dish",
    "typical_ingredients": ["cheese", "wine", "garlic", "bread"],
    "description": "Melted cheese served with chunks of bread for dipping.",
    "tags": ["creamy", "social", "traditional"]
},
 {
    "name": "Raclette",
    "cuisine": "Swiss",
    "meal_type": "Main Course",
    "category": "Cheese Dish",
    "typical_ingredients": ["raclette cheese", "potatoes", "pickles", "onions", "cheeese", "dairy"],
    "description": "Warm, melted cheese scraped over boiled potatoes and served with pickles.",
    "tags": ["melty", "comforting", "hearty"]
},
 {
    "name": "Rösti",
    "cuisine": "Swiss",
    "meal_type": "Side Dish",
    "category": "Potato Dish",
    "typical_ingredients": ["potatoes", "butter", "salt", "pepper"],
    "description": "A crispy, grated potato pancake, often enjoyed as a side or main.",
    "tags": ["crispy", "simple", "hearty"]
},
 {
    "name": "Zürcher Geschnetzeltes",
    "cuisine": "Swiss",
    "meal_type": "Main Course",
    "category": "Meat Dish",
    "typical_ingredients": ["veal", "cream", "mushrooms", "onions", "spices"],
    "description": "Tender strips of veal in a creamy mushroom sauce, a Swiss specialty.",
    "tags": ["creamy", "savory", "delicate"]
},
 {
    "name": "Älplermagronen",
    "cuisine": "Swiss",
    "meal_type": "Main Course",
    "category": "Pasta Dish",
    "typical_ingredients": ["pasta", "potatoes", "cheese", "cream", "onions"],
    "description": "A hearty casserole of pasta, potatoes, and cheese.",
    "tags": ["hearty", "comforting", "cheesy"]
},
 {
    "name": "Birchermüesli",
    "cuisine": "Swiss",
    "meal_type": "Breakfast",
    "category": "Breakfast",
    "typical_ingredients": ["oats", "yogurt", "fruits", "nuts", "honey"],
    "description": "A wholesome muesli with fruits and nuts, traditionally enjoyed at breakfast.",
    "tags": ["healthy", "fresh", "wholesome"]
},
 {
    "name": "Papet Vaudois",
    "cuisine": "Swiss",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["leeks", "potatoes", "sausage", "cream", "spices"],
    "description": "A comforting leek and potato stew often paired with sausage.",
    "tags": ["creamy", "hearty", "traditional"]
},
 {
    "name": "Capuns",
    "cuisine": "Swiss",
    "meal_type": "Main Course",
    "category": "Wrapped Dish",
    "typical_ingredients": ["Swiss chard", "meat", "spices", "dough"],
    "description": "Swiss chard parcels stuffed with a savory meat filling.",
    "tags": ["savory", "traditional", "wrapped"]
},
{
    "name": "Bündner Gerstensuppe",
    "cuisine": "Swiss",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["barley", "vegetables", "meat stock", "herbs"],
    "description": "A nourishing barley soup from the Graubünden region.",
    "tags": ["hearty", "wholesome", "traditional"]
},
 {
    "name": "Basler Läckerli",
    "cuisine": "Swiss",
    "meal_type": "Dessert",
    "category": "Dessert",
    "typical_ingredients": ["honey", "almonds", "spices", "sugar", "flour"],
    "description": "A spiced gingerbread cookie that is a beloved Swiss treat.",
    "tags": ["spiced", "sweet", "traditional"]
},

#Argentine
 {
    "name": "Asado",
    "cuisine": "Argentine",
    "meal_type": "Main Course",
    "category": "Barbecue",
    "typical_ingredients": ["meat", "chimichurri", "salt", "spices"],
    "description": "A traditional Argentine barbecue featuring a variety of grilled meats.",
    "tags": ["grilled", "savory", "meaty"]
},
 {
    "name": "Empanadas",
    "cuisine": "Argentine",
    "meal_type": "Main Course",
    "category": "Pastry",
    "typical_ingredients": ["flour", "meat", "onions", "spices", "egg"],
    "description": "Savory pastries filled with spiced meat or vegetables.",
    "tags": ["handheld", "savory", "crispy"]
},
 {
    "name": "Milanesa",
    "cuisine": "Argentine",
    "meal_type": "Main Course",
    "category": "Fried Meat",
    "typical_ingredients": ["beef","chicken", "breadcrumbs", "egg", "spices"],
    "description": "Breaded and fried meat cutlet, a popular Argentine dish.",
    "tags": ["crispy", "tender", "comfort food"]
},
 {
    "name": "Choripán",
    "cuisine": "Argentine",
    "meal_type": "Main Course",
    "category": "Sandwich",
    "typical_ingredients": ["chorizo", "bread", "chimichurri", "onions", "garic", "vinegar"],
    "description": "Grilled chorizo sausage served in crusty bread with condiments.",
    "tags": ["grilled", "spicy", "street food"]
},
 {
    "name": "Provoleta",
    "cuisine": "Argentine",
    "meal_type": "Appetizer",
    "category": "Cheese Dish",
    "typical_ingredients": ["provolone cheese", "oregano", "olive oil", "bread"],
    "description": "Melted provolone cheese often served as a starter in Argentine asado.",
    "tags": ["cheesy", "grilled", "savory"]
},
 {
    "name": "Locro",
    "cuisine": "Argentine",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["beans", "meat", "corn", "pumpkin", "spices"],
    "description": "A hearty stew of meat, beans, and corn, traditional to Argentina.",
    "tags": ["hearty", "stew", "comforting"]
},
 {
    "name": "Matambre a la Pizza",
    "cuisine": "Argentine",
    "meal_type": "Main Course",
    "category": "Meat Dish",
    "typical_ingredients": ["steak", "tomato sauce", "cheese", "herbs"],
    "description": "Thinly sliced steak topped with pizza-like ingredients.",
    "tags": ["fusion", "savory", "innovative"]
},
 {
    "name": "Carbonada Criolla",
    "cuisine": "Argentine",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["meat", "fruits", "vegetables", "potatoes", "spices"],
    "description": "A rich, slow-cooked stew blending meat with sweet fruits and vegetables.",
    "tags": ["sweet", "hearty", "rustic"]
},
 {
    "name": "Puchero",
    "cuisine": "Argentine",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["meat", "vegetables", "chickpeas", "potatoes", "spices"],
    "description": "A comforting stew combining various meats and seasonal vegetables.",
    "tags": ["hearty", "comforting", "traditional"]
},
 {
    "name": "Humita en Chala",
    "cuisine": "Argentine",
    "meal_type": "Main Course",
    "category": "Steamed Corn Pudding",
    "typical_ingredients": ["corn", "cheese", "cream", "spices"],
    "description": "A sweet corn pudding steamed in corn husks, reflecting indigenous influences.",
    "tags": ["sweet", "creamy", "unique"]
},

#Peruvian
 {
    "name": "Ceviche",
    "cuisine": "Peruvian",
    "meal_type": "Main Course",
    "category": "Seafood Dish",
    "typical_ingredients": ["fish", "lime", "chili", "onions", "cilantro"],
    "description": "Fresh fish marinated in citrus juices with a spicy kick.",
    "tags": ["fresh", "tangy", "zesty"]
},
 {
    "name": "Lomo Saltado",
    "cuisine": "Peruvian",
    "meal_type": "Main Course",
    "category": "Stir-fry",
    "typical_ingredients": ["beef", "onions", "tomatoes", "fries", "soy sauce"],
    "description": "A stir-fry combining beef, vegetables, and crispy fries in a savory sauce.",
    "tags": ["stir-fried", "savory", "fusion"]
},
 {
    "name": "Anticuchos",
    "cuisine": "Peruvian",
    "meal_type": "Main Course",
    "category": "Grilled Skewers",
    "typical_ingredients": ["beef heart", "vinegar", "spices", "herbs"],
    "description": "Marinated and grilled skewers, traditionally made with beef heart.",
    "tags": ["grilled", "tender", "traditional"]
},
 {
    "name": "Aji de Gallina",
    "cuisine": "Peruvian",
    "meal_type": "Main Course",
    "category": "Chicken Dish",
    "typical_ingredients": ["chicken", "cream", "bread", "spices", "nuts"],
    "description": "Shredded chicken in a mildly spicy, creamy sauce.",
    "tags": ["creamy", "spicy", "comforting"]
},
 {
    "name": "Causa Limeña",
    "cuisine": "Peruvian",
    "meal_type": "Main Course",
    "category": "Cold Potato Dish",
    "typical_ingredients": ["potatoes", "lime", "avocado", "chicken", "spices"],
    "description": "A layered dish of mashed potatoes with tangy fillings.",
    "tags": ["tangy", "colorful", "refreshing"]
},
 {
    "name": "Pollo a la Brasa",
    "cuisine": "Peruvian",
    "meal_type": "Main Course",
    "category": "Rotisserie Chicken",
    "typical_ingredients": ["chicken", "spices", "herbs", "garlic"],
    "description": "Peruvian-style rotisserie chicken with a smoky, savory flavor.",
    "tags": ["grilled", "savory", "juicy"]
},
 {
    "name": "Rocoto Relleno",
    "cuisine": "Peruvian",
    "meal_type": "Main Course",
    "category": "Stuffed Pepper",
    "typical_ingredients": ["peppers", "meat", "vegetables", "cheese", "spices"],
    "description": "Spicy red peppers stuffed with a flavorful mix of meat and vegetables.",
    "tags": ["spicy", "stuffed", "hearty"]
},
{
    "name": "Tiradito",
    "cuisine": "Peruvian",
    "meal_type": "Main Course",
    "category": "Raw Fish Dish",
    "typical_ingredients": ["fish", "citrus", "chilli", "oil", "herbs"],
    "description": "Thinly sliced raw fish drizzled with a zesty citrus dressing.",
    "tags": ["fresh", "tangy", "light"]
},
 {
    "name": "Papa a la Huancaína",
    "cuisine": "Peruvian",
    "meal_type": "Main Course",
    "category": "Potato Dish",
    "typical_ingredients": ["boiled potatoes", "cheese", "ají amarillo", "milk", "spices", "dairy"],
    "description": "Boiled potatoes smothered in a spicy, cheesy sauce.",
    "tags": ["creamy", "spicy", "comforting"]
},
 {
    "name": "Seco de Carne",
    "cuisine": "Peruvian",
    "meal_type": "Main Course",
    "category": "Meat Stew",
    "typical_ingredients": ["beef", "cilantro", "spices", "vegetables", "wine"],
    "description": "A slow-cooked beef stew infused with cilantro and a medley of spices.",
    "tags": ["hearty", "aromatic", "rich"]
},

#Chilean
 {
    "name": "Empanadas de Pino",
    "cuisine": "Chilean",
    "meal_type": "Main Course",
    "category": "Pastry",
    "typical_ingredients": ["flour", "beef", "onions", "olives", "spices"],
    "description": "Beef-stuffed pastries seasoned with onions and olives.",
    "tags": ["savory", "handheld", "traditional"]
},
 {
    "name": "Pastel de Choclo",
    "cuisine": "Chilean",
    "meal_type": "Main Course",
    "category": "Corn Pie",
    "typical_ingredients": ["corn", "meat", "onions", "olives", "spices"],
    "description": "A sweet and savory pie made with corn and a filling of meat and vegetables.",
    "tags": ["sweet", "savory", "hearty"]
},
 {
    "name": "Cazuela",
    "cuisine": "Chilean",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["meat", "potatoes", "pumpkin", "vegetables", "spices"],
    "description": "A hearty stew featuring meat and seasonal vegetables.",
    "tags": ["hearty", "comforting", "traditional"]
},
 {
    "name": "Completo",
    "cuisine": "Chilean",
    "meal_type": "Main Course",
    "category": "Hot Dog",
    "typical_ingredients": ["bread", "sausage", "avocado", "tomatoes", "mayonnaise"],
    "description": "A loaded hot dog topped with avocado, tomatoes, and mayonnaise.",
    "tags": ["filling", "street food", "fusion"]
},
 {
    "name": "Charquicán",
    "cuisine": "Chilean",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["meat", "vegetables", "corn", "potatoes", "spices"],
    "description": "A rustic stew combining dried meat with vegetables and corn.",
    "tags": ["hearty", "rustic", "savory"]
},
 {
    "name": "Porotos Granados",
    "cuisine": "Chilean",
    "meal_type": "Main Course",
    "category": "Bean Stew",
    "typical_ingredients": ["beans", "corn", "pumpkin", "tomatoes", "spices"],
    "description": "A bean stew enriched with fresh produce and seasonal flavors.",
    "tags": ["fresh", "hearty", "vegetarian"]
},
 {
    "name": "Caldillo de Congrio",
    "cuisine": "Chilean",
    "meal_type": "Main Course",
    "category": "Fish Soup",
    "typical_ingredients": ["conger eel", "tomatoes", "onions", "garlic", "spices"],
    "description": "A flavorful conger eel soup with a rich, savory broth.",
    "tags": ["seafood", "hearty", "aromatic"]
},
 {
    "name": "Sopaipillas",
    "cuisine": "Chilean",
    "meal_type": "Snack",
    "category": "Fried Dough",
    "typical_ingredients": ["flour", "pumpkin", "oil", "salt", "sugar"],
    "description": "Crispy fried dough that can be served savory with pebre or sweet with syrup.",
    "tags": ["crispy", "versatile", "fried"]
},
 {
    "name": "Chorrillana",
    "cuisine": "Chilean",
    "meal_type": "Main Course",
    "category": "Shared Dish",
    "typical_ingredients": ["fries", "beef", "onions", "eggs", "spices", "potatoes"],
    "description": "A hearty dish of fries topped with beef, onions, and eggs.",
    "tags": ["hearty", "sharing", "savory"]
},
 {
    "name": "Asado",
    "cuisine": "Chilean",
    "meal_type": "Main Course",
    "category": "Barbecue",
    "typical_ingredients": ["meats", "spices", "chimichurri", "salt"],
    "description": "Chilean-style barbecue featuring assorted grilled meats.",
    "tags": ["grilled", "savory", "festive"]
},

#Colombian
 {
    "name": "Arepas",
    "cuisine": "Colombian",
    "meal_type": "Main Course",
    "category": "Corn Cake",
    "typical_ingredients": ["cornmeal", "water", "salt", "butter", "cheese"],
    "description": "Versatile cornmeal cakes that can be grilled or fried and filled with various ingredients.",
    "tags": ["versatile", "traditional", "hearty"]
},
 {
    "name": "Bandeja Paisa",
    "cuisine": "Colombian",
    "meal_type": "Main Course",
    "category": "Platter",
    "typical_ingredients": ["beans", "rice", "meats", "avocado", "fried egg"],
    "description": "A generous platter featuring a variety of meats, rice, and beans.",
    "tags": ["hearty", "filling", "traditional"]
},
 {
    "name": "Ajiaco",
    "cuisine": "Colombian",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["chicken", "potatoes", "corn", "herbs", "crema"],
    "description": "A comforting chicken and potato soup enriched with local herbs.",
    "tags": ["hearty", "creamy", "traditional"]
},
 {
    "name": "Sancocho",
    "cuisine": "Colombian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["meat", "plantains", "yucca", "corn", "spices"],
    "description": "A traditional stew loaded with meat, plantains, and yucca.",
    "tags": ["hearty", "stew", "comforting"]
},
 {
    "name": "Empanadas",
    "cuisine": "Colombian",
    "meal_type": "Appetizer",
    "category": "Fried Pastry",
    "typical_ingredients": ["flour", "meat", "cheese", "potatoes", "spices"],
    "description": "Fried pastry pockets filled with savory meat or cheese.",
    "tags": ["crispy", "savory", "handheld"]
},
 {
    "name": "Tamales",
    "cuisine": "Colombian",
    "meal_type": "Main Course",
    "category": "Steamed Corn Dough",
    "typical_ingredients": ["corn dough", "meat", "vegetables", "spices", "banana leaves"],
    "description": "Steamed corn dough parcels filled with a flavorful meat and vegetable mix.",
    "tags": ["steamed", "traditional", "savory"]
},
 {
    "name": "Lechona",
    "cuisine": "Colombian",
    "meal_type": "Main Course",
    "category": "Roast Pig",
    "typical_ingredients": ["pork", "rice", "peas", "spices", "herbs"],
    "description": "Slow-roasted pig stuffed with rice and peas, a festive Colombian dish.",
    "tags": ["roasted", "hearty", "festive"]
},
 {
    "name": "Colombian-Style Ceviche",
    "cuisine": "Colombian",
    "meal_type": "Main Course",
    "category": "Seafood Dish",
    "typical_ingredients": ["fish", "lime", "onions", "cilantro", "chili"],
    "description": "A local twist on ceviche with fresh fish and a tangy dressing.",
    "tags": ["fresh", "tangy", "zesty"]
},
 {
    "name": "Arroz con Coco",
    "cuisine": "Colombian",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["rice", "coconut milk", "seafood", "spices", "herbs"],
    "description": "Coconut-infused rice typically paired with fresh seafood.",
    "tags": ["aromatic", "creamy", "exotic"]
},
 {
    "name": "Changua",
    "cuisine": "Colombian",
    "meal_type": "Breakfast",
    "category": "Breakfast Soup",
    "typical_ingredients": ["milk", "eggs", "water", "herbs", "bread"],
    "description": "A comforting breakfast soup made with milk, eggs, and herbs.",
    "tags": ["creamy", "warm", "simple"]
},

#Israeli
 {
    "name": "Falafel",
    "cuisine": "Israeli",
    "meal_type": "Main Course",
    "category": "Fritter",
    "typical_ingredients": ["chickpeas", "herbs", "spices", "flour"],
    "description": "Deep-fried chickpea patties served with tahini.",
    "tags": ["crispy", "savory", "vegetarian"]
},
 {
    "name": "Hummus",
    "cuisine": "Israeli",
    "meal_type": "Appetizer",
    "category": "Dip",
    "typical_ingredients": ["chickpeas", "tahini", "lemon", "garlic", "olive oil"],
    "description": "A creamy, blended chickpea dip often enjoyed with pita.",
    "tags": ["creamy", "smooth", "healthy"]
},
 {
    "name": "Shakshuka",
    "cuisine": "Israeli",
    "meal_type": "Main Course",
    "category": "Egg Dish",
    "typical_ingredients": ["eggs", "tomatoes", "peppers", "onions", "spices"],
    "description": "Eggs poached in a richly spiced tomato and pepper sauce.",
    "tags": ["hearty", "spicy", "brunch"]
},
 {
    "name": "Sabich",
    "cuisine": "Israeli",
    "meal_type": "Main Course",
    "category": "Sandwich",
    "typical_ingredients": ["pita", "eggplant", "boiled eggs", "salad", "tahini"],
    "description": "A pita sandwich filled with fried eggplant, hard-boiled eggs, and fresh salad.",
    "tags": ["street food", "savory", "balanced"]
},
 {
    "name": "Shawarma",
    "cuisine": "Israeli",
    "meal_type": "Main Course",
    "category": "Wrap",
    "typical_ingredients": ["spiced meat", "pita", "garlic sauce", "vegetables"],
    "description": "Thinly sliced, spiced meat wrapped in pita with fresh veggies.",
    "tags": ["spicy", "savory", "convenient"]
},
 {
    "name": "Israeli Salad",
    "cuisine": "Israeli",
    "meal_type": "Side Dish",
    "category": "Salad",
    "typical_ingredients": ["tomatoes", "cucumbers", "onions", "lemon", "olive oil"],
    "description": "A fresh, chopped salad dressed in lemon and olive oil.",
    "tags": ["fresh", "light", "healthy"]
},
 {
    "name": "Jachnun",
    "cuisine": "Israeli",
    "meal_type": "Breakfast",
    "category": "Pastry",
    "typical_ingredients": ["flour", "butter", "sugar"],
    "description": "A slow-cooked Yemenite pastry served with eggs and tomato sauce.",
    "tags": ["flaky", "buttery", "slow-cooked"]
},
 {
    "name": "Malawach",
    "cuisine": "Israeli",
    "meal_type": "Main Course",
    "category": "Fried Flatbread",
    "typical_ingredients": ["flour", "butter", "water", "salt"],
    "description": "A flaky fried flatbread with a crisp exterior.",
    "tags": ["crispy", "flaky", "traditional"]
},
 {
    "name": "Schnitzel",
    "cuisine": "Israeli",
    "meal_type": "Main Course",
    "category": "Breaded Meat",
    "typical_ingredients": ["meat", "breadcrumbs", "egg", "flour", "spices"],
    "description": "Breaded and fried meat cutlet with a crispy coating.",
    "tags": ["crispy", "tender", "savory"]
},
 {
    "name": "Bourekas",
    "cuisine": "Israeli",
    "meal_type": "Snack",
    "category": "Pastry",
    "typical_ingredients": ["dough", "cheese", "potatoes", "spices"],
    "description": "Savory pastries filled with cheese or potatoes, a popular street snack.",
    "tags": ["flaky", "savory", "light"]
},

#Jordanian

 {
    "name": "Mansaf",
    "cuisine": "Jordanian",
    "meal_type": "Main Course",
    "category": "Rice and Lamb Dish",
    "typical_ingredients": ["lamb", "jameed", "rice", "almonds", "spices", "dairy"],
    "description": "The national dish featuring lamb cooked in a tangy yogurt sauce over rice.",
    "tags": ["traditional", "rich", "hearty"]
},
{
    "name": "Maqluba",
    "cuisine": "Jordanian",
    "meal_type": "Main Course",
    "category": "Upside-down Rice Dish",
    "typical_ingredients": ["rice", "meat", "vegetables", "spices", "tomatoes"],
    "description": "A layered rice dish inverted to reveal a mix of meat and vegetables.",
    "tags": ["layered", "hearty", "unique"]
},
 {
    "name": "Mezze Platter",
    "cuisine": "Jordanian",
    "meal_type": "Appetizer",
    "category": "Assorted Dips",
    "typical_ingredients": ["hummus", "baba ganoush", "tabbouleh", "pita", "eggplant", "tahini", "olive oil", "lemon juice", "garlic", "wheat", "mint"],
    "description": "An assortment of small dishes and dips perfect for sharing.",
    "tags": ["varied", "flavorful", "social"]
},
 {
    "name": "Shish Kebab",
    "cuisine": "Jordanian",
    "meal_type": "Main Course",
    "category": "Grilled Meat",
    "typical_ingredients": ["lamb", "chicken", "spices", "vegetables", "skewers"],
    "description": "Marinated meat grilled on skewers, a staple of Middle Eastern cuisine.",
    "tags": ["grilled", "aromatic", "juicy"]
},
 {
    "name": "Warak Enab",
    "cuisine": "Jordanian",
    "meal_type": "Appetizer",
    "category": "Stuffed Grape Leaves",
    "typical_ingredients": ["grape leaves", "rice", "spices", "herbs", "minced meat"],
    "description": "Grape leaves stuffed with a flavorful rice and herb mixture.",
    "tags": ["fresh", "tangy", "traditional"]
},
 {
    "name": "Mujadara",
    "cuisine": "Jordanian",
    "meal_type": "Main Course",
    "category": "Lentil and Rice Dish",
    "typical_ingredients": ["lentils", "rice", "onions", "spices"],
    "description": "A simple, hearty dish of lentils and rice topped with caramelized onions.",
    "tags": ["hearty", "simple", "comforting"]
},
 {
    "name": "Musakhan",
    "cuisine": "Jordanian",
    "meal_type": "Main Course",
    "category": "Roasted Chicken",
    "typical_ingredients": ["chicken", "sumac", "onions", "flatbread", "spices"],
    "description": "Sumac-spiced roasted chicken served over flatbread with onions.",
    "tags": ["aromatic", "spiced", "traditional"]
},
 {
    "name": "Freekeh Soup",
    "cuisine": "Jordanian",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["roasted green wheat", "chicken", "vegetables", "spices", "wheat"],
    "description": "A smoky, nutty soup made from roasted green wheat.",
    "tags": ["smoky", "hearty", "nutty"]
},
 {
    "name": "Zarb",
    "cuisine": "Jordanian",
    "meal_type": "Main Course",
    "category": "Barbecue",
    "typical_ingredients": ["meat", "vegetables", "spices", "herbs"],
    "description": "Bedouin-style barbecue cooked in an underground oven.",
    "tags": ["smoky", "aromatic", "traditional"]
},
 {
    "name": "Falafel",
    "cuisine": "Jordanian",
    "meal_type": "Appetizer",
    "category": "Fritter",
    "typical_ingredients": ["chickpeas", "herbs", "spices", "flour"],
    "description": "Crispy chickpea fritters that are a staple in Jordanian mezze.",
    "tags": ["crispy", "flavorful", "vegetarian"]
},

#South African
 {
    "name": "Braai",
    "cuisine": "South African",
    "meal_type": "Main Course",
    "category": "Barbecue",
    "typical_ingredients": ["meats", "spices", "barbecue sauce"],
    "description": "A traditional South African barbecue featuring assorted grilled meats.",
    "tags": ["grilled", "savory", "social"]
},
 {
    "name": "Bobotie",
    "cuisine": "South African",
    "meal_type": "Main Course",
    "category": "Casserole",
    "typical_ingredients": ["minced meat", "spices", "egg", "dried fruits"],
    "description": "A spiced meat casserole topped with a sweet and savory custard.",
    "tags": ["sweet", "savory", "layered"]
},
 {
    "name": "Potjiekos",
    "cuisine": "South African",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["meat", "vegetables", "spices", "herbs"],
    "description": "A slow-cooked stew prepared in a cast-iron pot over an open fire.",
    "tags": ["hearty", "traditional", "slow-cooked"]
},
 {
    "name": "Bunny Chow",
    "cuisine": "South African",
    "meal_type": "Main Course",
    "category": "Street Food",
    "typical_ingredients": ["bread", "curry", "spices", "vegetables", "meat"],
    "description": "A hollowed-out loaf of bread filled with a spicy curry.",
    "tags": ["spicy", "filling", "street food"]
},
 {
    "name": "Cape Malay Curry",
    "cuisine": "South African",
    "meal_type": "Main Course",
    "category": "Curry",
    "typical_ingredients": ["meat", "spices", "coconut milk", "dried fruits"],
    "description": "A fragrant curry with a blend of sweet and savory Cape Malay flavors.",
    "tags": ["aromatic", "spiced", "exotic"]
},
 {
    "name": "Boerewors",
    "cuisine": "South African",
    "meal_type": "Main Course",
    "category": "Sausage",
    "typical_ingredients": ["pork", "spices", "herbs", "casings"],
    "description": "A traditional South African sausage seasoned with a blend of herbs and spices.",
    "tags": ["grilled", "spiced", "hearty"]
},
 {
    "name": "Sosaties",
    "cuisine": "South African",
    "meal_type": "Main Course",
    "category": "Skewers",
    "typical_ingredients": ["meat", "fruit", "spices", "skewers", "herbs"],
    "description": "Marinated meat skewers often interspersed with dried fruits and vegetables.",
    "tags": ["grilled", "sweet", "savory"]
},
{
    "name": "Pap and Chakalaka",
    "cuisine": "South African",
    "meal_type": "Side Dish",
    "category": "Side Dish",
    "typical_ingredients": ["maize porridge", "vegetable relish", "spices", "tomatoes", "cornstarch"],
    "description": "A comforting combination of maize porridge served with a spicy vegetable relish.",
    "tags": ["hearty", "spicy", "traditional"]
},
 {
    "name": "Vetkoek with Curried Filling",
    "cuisine": "South African",
    "meal_type": "Main Course",
    "category": "Fried Bread",
    "typical_ingredients": ["flour", "oil", "curry", "spices", "meat", "vegetables"],
    "description": "Deep-fried dough pockets stuffed with a savory curried filling.",
    "tags": ["crispy", "spiced", "filling"]
},
 {
    "name": "Umngqusho",
    "cuisine": "South African",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["samp", "beans", "spices", "herbs", "meat", "corn"],
    "description": "A traditional dish of samp and beans cooked with rich, earthy flavors.",
    "tags": ["hearty", "traditional", "nutritious"]
},

#New Zealand
 {
    "name": "Hangi",
    "cuisine": "New Zealand",
    "meal_type": "Main Course",
    "category": "Earth-cooked Dish",
    "typical_ingredients": ["meat", "vegetables", "herbs", "smoke"],
    "description": "A traditional Māori meal cooked in an earth oven with a mix of meats and root vegetables.",
    "tags": ["earthy", "smoky", "traditional"]
},
 {
    "name": "Roast Lamb",
    "cuisine": "New Zealand",
    "meal_type": "Main Course",
    "category": "Roast",
    "typical_ingredients": ["lamb", "rosemary", "garlic", "olive oil", "spices"],
    "description": "Succulent roast lamb seasoned with herbs and garlic.",
    "tags": ["roasted", "tender", "aromatic"]
},
 {
    "name": "Meat Pie",
    "cuisine": "New Zealand",
    "meal_type": "Main Course",
    "category": "Pie",
    "typical_ingredients": ["meat", "pastry", "gravy", "vegetables", "spices"],
    "description": "A savory pie filled with seasoned meat and rich gravy.",
    "tags": ["hearty", "comforting", "savory"]
},
 {
    "name": "Fish and Chips",
    "cuisine": "New Zealand",
    "meal_type": "Main Course",
    "category": "Fried Dish",
    "typical_ingredients": ["fish", "potatoes", "flour", "oil", "salt"],
    "description": "Crispy battered fish served with golden fries.",
    "tags": ["crispy", "classic", "fried"]
},
{
    "name": "Whitebait Fritters",
    "cuisine": "New Zealand",
    "meal_type": "Main Course",
    "category": "Fritters",
    "typical_ingredients": ["whitebait", "egg", "flour", "herbs", "oil", "fish"],
    "description": "Delicate fritters made from small whitebait fish, lightly fried.",
    "tags": ["crispy", "delicate", "fresh"]
},
 {
    "name": "Lamb Burger",
    "cuisine": "New Zealand",
    "meal_type": "Main Course",
    "category": "Burger",
    "typical_ingredients": ["lamb", "bread", "lettuce", "tomato", "spices"],
    "description": "A gourmet burger featuring a flavorful lamb patty and fresh toppings.",
    "tags": ["juicy", "savory", "modern"]
},
 {
    "name": "Seafood Chowder",
    "cuisine": "New Zealand",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["seafood", "cream", "potatoes", "onions", "herbs"],
    "description": "A creamy stew packed with a variety of fresh seafood.",
    "tags": ["creamy", "hearty", "seafood"]
},
 {
    "name": "Crayfish Boil",
    "cuisine": "New Zealand",
    "meal_type": "Main Course",
    "category": "Boiled Seafood",
    "typical_ingredients": ["crayfish", "spices", "lemon", "herbs", "salt"],
    "description": "Simply prepared crayfish boiled with spices and served with dipping sauce.",
    "tags": ["fresh", "savory", "simple"]
},
{
    "name": "Kumara Soup",
    "cuisine": "New Zealand",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["kumara", "vegetables", "cream", "spices", "herbs", "potatoes"],
    "description": "A velvety soup made from New Zealand sweet potatoes (kumara) and seasonal vegetables.",
    "tags": ["creamy", "hearty", "seasonal"]
},
 {
    "name": "Lamb Stew",
    "cuisine": "New Zealand",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["lamb", "vegetables", "red wine", "herbs", "spices"],
    "description": "A hearty, slow-cooked lamb stew enriched with seasonal vegetables.",
    "tags": ["hearty", "rich", "slow-cooked"]
},

#Scandinavian

 {
    "name": "Swedish Meatballs",
    "cuisine": "Scandinavian",
    "meal_type": "Main Course",
    "category": "Meatballs",
    "typical_ingredients": ["meat", "breadcrumbs", "cream", "spices", "lingonberry"],
    "description": "Tender meatballs served with a creamy sauce and lingonberry jam.",
    "tags": ["creamy", "savory", "comforting"]
},
 {
    "name": "Danish Smørrebrød",
    "cuisine": "Scandinavian",
    "meal_type": "Main Course",
    "category": "Open Sandwich",
    "typical_ingredients": ["bread", "toppings", "butter", "herbs"],
    "description": "Artfully assembled open-faced sandwiches with a variety of toppings.",
    "tags": ["fresh", "creative", "traditional"]
},
 {
    "name": "Norwegian Gravlax",
    "cuisine": "Scandinavian",
    "meal_type": "Appetizer",
    "category": "Cured Fish",
    "typical_ingredients": ["salmon", "salt", "sugar", "dill", "lemon"],
    "description": "Cured salmon served with a tangy mustard-dill sauce.",
    "tags": ["fresh", "tangy", "delicate"]
},
 {
    "name": "Danish Frikadeller",
    "cuisine": "Scandinavian",
    "meal_type": "Main Course",
    "category": "Meatballs",
    "typical_ingredients": ["pork", "onions", "breadcrumbs", "egg", "spices"],
    "description": "Pan-fried meatballs with a savory blend of spices.",
    "tags": ["savory", "hearty", "traditional"]
},
 {
    "name": "Swedish Jansson's Temptation",
    "cuisine": "Scandinavian",
    "meal_type": "Main Course",
    "category": "Casserole",
    "typical_ingredients": ["potatoes", "anchovies", "cream", "onions", "bread"],
    "description": "A creamy potato casserole with a hint of anchovy flavor.",
    "tags": ["creamy", "savory", "comforting"]
},
 {
    "name": "Danish Stegt Flæsk",
    "cuisine": "Scandinavian",
    "meal_type": "Main Course",
    "category": "Pork Dish",
    "typical_ingredients": ["pork", "potatoes", "parsley", "salt", "pepper"],
    "description": "Crispy pork slices served with boiled potatoes and parsley sauce.",
    "tags": ["crispy", "savory", "hearty"]
},
 {
    "name": "Norwegian Rakfisk",
    "cuisine": "Scandinavian",
    "meal_type": "Main Course",
    "category": "Fermented Fish",
    "typical_ingredients": ["trout", "salt", "water", "fermentation culture"],
    "description": "Fermented trout served with flatbread, a traditional Norwegian delicacy.",
    "tags": ["fermented", "traditional", "bold"]
},
 {
    "name": "Swedish Pickled Herring",
    "cuisine": "Scandinavian",
    "meal_type": "Appetizer",
    "category": "Fish Dish",
    "typical_ingredients": ["herring", "vinegar", "onions", "spices", "sugar", "fish"],
    "description": "Marinated herring often served with potatoes and dill.",
    "tags": ["tangy", "savory", "traditional"]
},
 {
    "name": "Danish Æbleskiver",
    "cuisine": "Scandinavian",
    "meal_type": "Dessert",
    "category": "Pancake Balls",
    "typical_ingredients": ["flour", "egg", "milk", "apples", "sugar"],
    "description": "Light, spherical pancakes dusted with powdered sugar.",
    "tags": ["sweet", "fluffy", "traditional"]
},
 {
    "name": "Norwegian Rømmegrøt",
    "cuisine": "Scandinavian",
    "meal_type": "Main Course",
    "category": "Porridge",
    "typical_ingredients": ["sour cream", "flour", "milk", "butter", "sugar"],
    "description": "A rich sour cream porridge traditionally drizzled with sugar and cinnamon.",
    "tags": ["creamy", "rich", "comforting"]
},

#Kenyan 
 {
    "name": "Nyama Choma",
    "cuisine": "Kenyan",
    "meal_type": "Main Course",
    "category": "Grilled Meat",
    "typical_ingredients": ["goat", "beef", "salt", "spices", "lemon"],
    "description": "Grilled meat, typically goat or beef, seasoned simply with salt and spices.",
    "tags": ["grilled", "savory", "traditional"]
},
 {
    "name": "Ugali",
    "cuisine": "Kenyan",
    "meal_type": "Main Course",
    "category": "Staple",
    "typical_ingredients": ["maize flour", "water", "salt"],
    "description": "A dense maize porridge that forms the staple of many Kenyan meals.",
    "tags": ["simple", "filling", "staple"]
},
 {
    "name": "Sukuma Wiki",
    "cuisine": "Kenyan",
    "meal_type": "Side Dish",
    "category": "Vegetable Dish",
    "typical_ingredients": ["collard greens", "onions", "tomatoes", "spices"],
    "description": "Sautéed collard greens flavored with onions and tomatoes.",
    "tags": ["healthy", "green", "savory"]
},
 {
    "name": "Githeri",
    "cuisine": "Kenyan",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["maize", "beans", "vegetables", "spices"],
    "description": "A hearty mix of boiled maize and beans seasoned with local spices.",
    "tags": ["hearty", "filling", "traditional"]
},
 {
    "name": "Chapati",
    "cuisine": "Kenyan",
    "meal_type": "Side Dish",
    "category": "Flatbread",
    "typical_ingredients": ["flour", "water", "oil", "salt"],
    "description": "A soft, layered flatbread influenced by Indian cuisine.",
    "tags": ["soft", "versatile", "flaky"]
},
 {
    "name": "Mandazi",
    "cuisine": "Kenyan",
    "meal_type": "Snack",
    "category": "Fried Dough",
    "typical_ingredients": ["flour", "sugar", "coconut milk", "oil", "yeast"],
    "description": "Slightly sweet, fried dough enjoyed as a snack or breakfast treat.",
    "tags": ["sweet", "fried", "treat"]
},
 {
    "name": "Irio",
    "cuisine": "Kenyan",
    "meal_type": "Side Dish",
    "category": "Mashed Dish",
    "typical_ingredients": ["peas", "potatoes", "corn", "butter", "salt"],
    "description": "A nutritious mash of peas, potatoes, and corn, often served as a side.",
    "tags": ["creamy", "hearty", "traditional"]
},
 {
    "name": "Samosas",
    "cuisine": "Kenyan",
    "meal_type": "Appetizer",
    "category": "Appetizer",
    "typical_ingredients": ["flour", "potatoes", "peas", "spices", "meat"],
    "description": "Deep-fried pastry pockets filled with spiced vegetables or meat.",
    "tags": ["crispy", "spiced", "popular"]
},
 {
    "name": "Mutura",
    "cuisine": "Kenyan",
    "meal_type": "Main Course",
    "category": "Sausage",
    "typical_ingredients": ["meat", "spices", "casings", "herbs"],
    "description": "A local sausage made from spiced meat, often grilled to perfection.",
    "tags": ["grilled", "spicy", "traditional"]
},
 {
    "name": "Mishkaki",
    "cuisine": "Kenyan",
    "meal_type": "Main Course",
    "category": "Grilled Skewers",
    "typical_ingredients": ["marinated meat", "spices", "skewers", "lemongrass", "meat"],
    "description": "Skewered and grilled marinated meat, a popular street food.",
    "tags": ["grilled", "flavorful", "savory"]
},

#Senegeelse 
 {
    "name": "Thieboudienne",
    "cuisine": "Senegalese",
    "meal_type": "Main Course",
    "category": "Fish and Rice Dish",
    "typical_ingredients": ["fish", "rice", "tomatoes", "vegetables", "spices"],
    "description": "Senegal's national dish featuring fish and rice stewed in a tomato sauce.",
    "tags": ["hearty", "savory", "traditional"]
},
 {
    "name": "Yassa Poulet",
    "cuisine": "Senegalese",
    "meal_type": "Main Course",
    "category": "Chicken Dish",
    "typical_ingredients": ["chicken", "onions", "lemon", "mustard", "spices"],
    "description": "Marinated chicken simmered in a tangy onion-lemon sauce.",
    "tags": ["tangy", "savory", "aromatic"]
},
 {
    "name": "Yassa Poisson",
    "cuisine": "Senegalese",
    "meal_type": "Main Course",
    "category": "Fish Dish",
    "typical_ingredients": ["fish", "onions", "lemon", "mustard", "spices"],
    "description": "A fish variant of Yassa with a vibrant, citrusy flavor.",
    "tags": ["tangy", "fresh", "savory"]
},
 {
    "name": "Mafé",
    "cuisine": "Senegalese",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["meat", "fish", "peanut butter", "tomatoes", "spices", "vegetables"],
    "description": "A rich stew featuring a creamy peanut sauce with meat or fish.",
    "tags": ["creamy", "nutty", "hearty"]
},
 {
    "name": "Soupou Kandja",
    "cuisine": "Senegalese",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["okra", "tomatoes", "meat", "spices", "onions"],
    "description": "An okra-based stew enriched with tomatoes and spices.",
    "tags": ["thick", "savory", "traditional"]
},
 {
    "name": "Dibi",
    "cuisine": "Senegalese",
    "meal_type": "Main Course",
    "category": "Grilled Meat",
    "typical_ingredients": ["lamb", "mutton", "spices", "lemons", "herbs"],
    "description": "Grilled lamb or mutton served with a side of spicy condiments.",
    "tags": ["grilled", "spiced", "savory"]
},
 {
    "name": "Accara",
    "cuisine": "Senegalese",
    "meal_type": "Appetizer",
    "category": "Fritter",
    "typical_ingredients": ["black-eyed peas", "onions", "spices", "flour"],
    "description": "Savory fritters made from black-eyed peas, a popular street snack.",
    "tags": ["crispy", "savory", "traditional"]
},
 {
    "name": "Fataya",
    "cuisine": "Senegalese",
    "meal_type": "Appetizer",
    "category": "Pastry",
    "typical_ingredients": ["flour", "meat", "onions", "spices", "oil"],
    "description": "Fried pastry turnovers filled with spiced meat or fish.",
    "tags": ["crispy", "savory", "handheld"]
},
 {
    "name": "Ndambé",
    "cuisine": "Senegalese",
    "meal_type": "Main Course",
    "category": "Bean Stew",
    "typical_ingredients": ["beans", "tomatoes", "spices", "onions", "garlic"],
    "description": "A hearty bean stew enjoyed for its robust flavor.",
    "tags": ["hearty", "spiced", "filling"]
},
 {
    "name": "Thiakry",
    "cuisine": "Senegalese",
    "meal_type": "Dessert",
    "category": "Pudding",
    "typical_ingredients": ["millet", "milk", "sugar", "raisins", "spices", "cereal", "grain"],
    "description": "A sweet millet pudding served as a dessert or side dish.",
    "tags": ["sweet", "creamy", "unique"]
},

#Tunisian
 {
    "name": "Couscous",
    "cuisine": "Tunisian",
    "meal_type": "Main Course",
    "category": "Steamed Grain Dish",
    "typical_ingredients": ["semolina", "meat", "vegetables", "spices", "broth"],
    "description": "Steamed semolina served with a medley of vegetables and meat.",
    "tags": ["fluffy", "hearty", "traditional"]
},
 {
    "name": "Brik",
    "cuisine": "Tunisian",
    "meal_type": "Appetizer",
    "category": "Pastry",
    "typical_ingredients": ["dough", "egg", "tuna", "capers", "spices"],
    "description": "Crispy pastry wrapped around egg and tuna, deep-fried to perfection.",
    "tags": ["crispy", "savory", "light"]
},
 {
    "name": "Lablabi",
    "cuisine": "Tunisian",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["chickpeas", "garlic", "cumin", "harissa", "bread", "peppers"],
    "description": "A robust chickpea soup with garlic, cumin, and a kick of harissa.",
    "tags": ["spicy", "hearty", "comforting"]
},
 {
    "name": "Shakshouka",
    "cuisine": "Tunisian",
    "meal_type": "Main Course",
    "category": "Egg Dish",
    "typical_ingredients": ["eggs", "tomatoes", "peppers", "onions", "spices"],
    "description": "Eggs poached in a spicy tomato and pepper stew.",
    "tags": ["hearty", "spicy", "comforting"]
},
 {
    "name": "Harissa",
    "cuisine": "Tunisian",
    "meal_type": "Condiment",
    "category": "Condiment",
    "typical_ingredients": ["chili peppers", "garlic", "cumin", "olive oil"],
    "description": "A fiery chili paste essential to Tunisian cuisine.",
    "tags": ["spicy", "fiery", "intense"]
},
 {
    "name": "Mloukhia",
    "cuisine": "Tunisian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["beef", "green herbs", "spices", "tomatoes", "garlic"],
    "description": "A slow-cooked beef stew in a thick, herb-infused sauce.",
    "tags": ["rich", "hearty", "aromatic"]
},
 {
    "name": "Tunisian Mechouia Salad",
    "cuisine": "Tunisian",
    "meal_type": "Appetizer",
    "category": "Salad",
    "typical_ingredients": ["grilled peppers", "tomatoes", "onions", "garlic", "olive oil"],
    "description": "A smoky salad of grilled vegetables blended with spices.",
    "tags": ["smoky", "fresh", "vibrant"]
},
 {
    "name": "Ojja",
    "cuisine": "Tunisian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["tomatoes", "sausage", "eggs", "spices", "onions"],
    "description": "A spicy tomato stew featuring merguez sausage and eggs.",
    "tags": ["spicy", "hearty", "robust"]
},
 {
    "name": "Kamounia",
    "cuisine": "Tunisian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["lamb", "beef", "cumin", "tomatoes", "spices", "herbs"],
    "description": "A lamb or beef stew richly spiced with cumin and local herbs.",
    "tags": ["spicy", "aromatic", "rich"]
},
 {
    "name": "Tajine",
    "cuisine": "Tunisian",
    "meal_type": "Main Course",
    "category": "Baked Dish",
    "typical_ingredients": ["meat", "vegetables", "spices", "olive oil", "herbs"],
    "description": "A hearty baked dish of meat and vegetables prepared in a traditional clay pot.",
    "tags": ["slow-cooked", "aromatic", "traditional"]
},

#Ivorian 
 {
    "name": "Attiéké",
    "cuisine": "Ivorian",
    "meal_type": "Main Course",
    "category": "Cassava Couscous",
    "typical_ingredients": ["cassava", "salt", "water", "vegetables", "spices"],
    "description": "A fermented cassava couscous typically served with grilled fish or meat.",
    "tags": ["fluffy", "traditional", "light"]
},
 {
    "name": "Alloco",
    "cuisine": "Ivorian",
    "meal_type": "Snack",
    "category": "Snack",
    "typical_ingredients": ["plantains", "oil", "salt", "pepper"],
    "description": "Fried ripe plantain slices served with a spicy dipping sauce.",
    "tags": ["crispy", "sweet", "savory"]
},
 {
    "name": "Kedjenou",
    "cuisine": "Ivorian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["chicken", "vegetables", "spices", "herbs", "oil"],
    "description": "A slow-cooked chicken stew with a rich blend of spices and vegetables.",
    "tags": ["hearty", "spiced", "traditional"]
},
 {
    "name": "Garba",
    "cuisine": "Ivorian",
    "meal_type": "Main Course",
    "category": "Street Food",
    "typical_ingredients": ["attiéké", "tuna", "spices", "salad"],
    "description": "A popular street dish pairing attiéké with seasoned tuna and salad.",
    "tags": ["fresh", "savory", "light"]
},
 {
    "name": "Sauce Graine",
    "cuisine": "Ivorian",
    "meal_type": "Side Dish",
    "category": "Sauce",
    "typical_ingredients": ["palm nuts", "tomatoes", "spices", "herbs"],
    "description": "A rich palm nut sauce served with rice or fufu.",
    "tags": ["rich", "nutty", "savory"]
},
 {
    "name": "Placali",
    "cuisine": "Ivorian",
    "meal_type": "Main Course",
    "category": "Staple",
    "typical_ingredients": ["cassava", "water", "salt"],
    "description": "A dough-like staple made from fermented cassava, commonly eaten with stews.",
    "tags": ["dense", "traditional", "filling"]
},
 {
    "name": "Riz Sauce",
    "cuisine": "Ivorian",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["rice", "meat sauce", "vegetables", "spices"],
    "description": "Rice served with a flavorful meat and vegetable sauce.",
    "tags": ["savory", "hearty", "traditional"]
},
 {
    "name": "Fufu",
    "cuisine": "Ivorian",
    "meal_type": "Main Course",
    "category": "Staple",
    "typical_ingredients": ["cassava", "plantains", "water", "salt"],
    "description": "A starchy, pounded dough served with hearty stews.",
    "tags": ["dense", "traditional", "versatile"]
},
 {
    "name": "Grilled Tilapia",
    "cuisine": "Ivorian",
    "meal_type": "Main Course",
    "category": "Grilled Fish",
    "typical_ingredients": ["tilapia", "spices", "lemon", "herbs", "fish"],
    "description": "Fresh tilapia grilled with a blend of spices and citrus.",
    "tags": ["grilled", "light", "savory"]
},
 {
    "name": "Gombo Soup",
    "cuisine": "Ivorian",
    "meal_type": "Main Course",
    "category": "Soup",
    "typical_ingredients": ["okra", "meat", "spices", "tomatoes", "onions"],
    "description": "A hearty okra-based soup enriched with local spices and meat.",
    "tags": ["hearty", "savory", "traditional"]
},

#Angolan
 {
    "name": "Muamba de Galinha",
    "cuisine": "Angolan",
    "meal_type": "Main Course",
    "category": "Chicken Stew",
    "typical_ingredients": ["chicken", "palm oil", "okra", "spices", "tomatoes"],
    "description": "A rich chicken stew cooked in palm oil with okra and spices.",
    "tags": ["rich", "hearty", "traditional"]
},
{
    "name": "Calulu",
    "cuisine": "Angolan",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["meat", "vegetables", "dried fish", "spices"],
    "description": "A flavorful stew featuring fish or meat with vegetables and dried fish.",
    "tags": ["hearty", "savory", "traditional"]
},
{
    "name": "Funje",
    "cuisine": "Angolan",
    "meal_type": "Main Course",
    "category": "Staple",
    "typical_ingredients": ["cassava", "flour", "water", "salt"],
    "description": "A cassava flour porridge similar to fufu, a staple in Angolan meals.",
    "tags": ["dense", "traditional", "filling"]
},
 {
    "name": "Mufete",
    "cuisine": "Angolan",
    "meal_type": "Main Course",
    "category": "Grilled Fish",
    "typical_ingredients": ["fish", "spices", "vegetables", "lemon"],
    "description": "Grilled fish served with boiled vegetables and a tangy sauce.",
    "tags": ["grilled", "savory", "fresh"]
},
 {
    "name": "Pirão",
    "cuisine": "Angolan",
    "meal_type": "Side Dish",
    "category": "Porridge",
    "typical_ingredients": ["fish", "broth", "cassava", "flour", "spices"],
    "description": "A thick porridge made by thickening fish broth with cassava flour.",
    "tags": ["thick", "hearty", "traditional"]
},
{
    "name": "Muamba de Peixe",
    "cuisine": "Angolan",
    "meal_type": "Main Course",
    "category": "Fish Stew",
    "typical_ingredients": ["fish", "palm oil", "spices", "vegetables"],
    "description": "A hearty fish stew prepared with palm oil and aromatic spices.",
    "tags": ["rich", "spicy", "traditional"]
},
 {
    "name": "Feijoada Angolana",
    "cuisine": "Angolan",
    "meal_type": "Main Course",
    "category": "Bean and Meat Stew",
    "typical_ingredients": ["beans", "meat", "spices", "tomatoes", "herbs"],
    "description": "A robust stew combining beans and meat with local spices.",
    "tags": ["hearty", "rich", "savory"]
},
 {
    "name": "Galinha Grelhada",
    "cuisine": "Angolan",
    "meal_type": "Main Course",
    "category": "Grilled Chicken",
    "typical_ingredients": ["chicken", "spices", "lemon", "herbs"],
    "description": "Simply grilled chicken marinated with herbs and spices.",
    "tags": ["grilled", "tender", "savory"]
},
 {
    "name": "Rice with Beans",
    "cuisine": "Angolan",
    "meal_type": "Main Course",
    "category": "Rice Dish",
    "typical_ingredients": ["rice", "beans", "spices", "herbs"],
    "description": "A comforting dish pairing savory rice with well-seasoned beans.",
    "tags": ["simple", "hearty", "traditional"]
},
 {
    "name": "Moqueca Angolana",
    "cuisine": "Angolan",
    "meal_type": "Main Course",
    "category": "Seafood Stew",
    "typical_ingredients": ["seafood", "coconut milk", "spices", "herbs", "tomatoes"],
    "description": "A regional take on seafood stew bursting with local flavors.",
    "tags": ["flavorful", "creamy", "spicy"]
},

#Albanian
 {
    "name": "Byrek",
    "cuisine": "Albanian",
    "meal_type": "Main Course",
    "category": "Pastry",
    "typical_ingredients": ["dough", "spinach", "cheese", "onions", "oil"],
    "description": "Flaky savory pastries filled with spinach, cheese, or meat.",
    "tags": ["flaky", "savory", "traditional"]
},
 {
    "name": "Tavë Kosi",
    "cuisine": "Albanian",
    "meal_type": "Main Course",
    "category": "Baked Dish",
    "typical_ingredients": ["lamb", "rice", "yogurt", "eggs", "herbs"],
    "description": "Baked lamb and rice in a tangy, custard-like yogurt sauce.",
    "tags": ["tangy", "creamy", "comforting"]
},
 {
    "name": "Fërgesë",
    "cuisine": "Albanian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["peppers", "tomatoes", "cheese", "onions", "spices"],
    "description": "A rich stew of peppers, tomatoes, and cheese, sometimes with meat.",
    "tags": ["rich", "savory", "hearty"]
},
 {
    "name": "Qofte",
    "cuisine": "Albanian",
    "meal_type": "Main Course",
    "category": "Meatballs",
    "typical_ingredients": ["minced meat", "herbs", "spices", "onions"],
    "description": "Spiced meatballs typically served with fresh salads or bread.",
    "tags": ["savory", "juicy", "traditional"]
},
 {
    "name": "Speca të Mbushura",
    "cuisine": "Albanian",
    "meal_type": "Main Course",
    "category": "Stuffed Vegetables",
    "typical_ingredients": ["peppers", "rice", "herbs", "minced meat"],
    "description": "Stuffed peppers filled with rice, herbs, and sometimes meat.",
    "tags": ["flavorful", "hearty", "traditional"]
},
{
    "name": "Pite",
    "cuisine": "Albanian",
    "meal_type": "Main Course",
    "category": "Pie",
    "typical_ingredients": ["flour", "vegetables", "meat", "spices", "oil"],
    "description": "Traditional Albanian pies or flatbreads filled with vegetables or meat.",
    "tags": ["flaky", "savory", "homemade"]
},
 {
    "name": "Jani me Fasule",
    "cuisine": "Albanian",
    "meal_type": "Main Course",
    "category": "Stew",
    "typical_ingredients": ["beans", "tomatoes", "herbs", "onions", "spices"],
    "description": "A comforting bean stew enjoyed across Albania.",
    "tags": ["hearty", "simple", "traditional"]
},
 {
    "name": "Flija",
    "cuisine": "Albanian",
    "meal_type": "Main Course",
    "category": "Layered Pancake",
    "typical_ingredients": ["flour", "water", "butter", "salt", "cream"],
    "description": "A unique layered pancake cooked over an open flame and served with sour cream.",
    "tags": ["layered", "savory", "traditional"]
},
 {
    "name": "Qifqi",
    "cuisine": "Albanian",
    "meal_type": "Main Course",
    "category": "Rice Ball",
    "typical_ingredients": ["rice", "herbs", "spices", "oil"],
    "description": "Savory rice balls flavored with herbs, representing a regional specialty.",
    "tags": ["savory", "hearty", "traditional"]
},
 {
    "name": "Baklava",
    "cuisine": "Albanian",
    "meal_type": "Dessert",
    "category": "Dessert",
    "typical_ingredients": ["dough", "nuts", "honey", "sugar", "butter"],
    "description": "Sweet, syrup-soaked pastry reflecting Ottoman influences in Albanian desserts.",
    "tags": ["sweet", "nutty", "decadent"]
}
]

'''

# Connect to MongoDB
try:
    client = MongoClient('mongodb://localhost:5500/')
    db = client['glo_eat_app']
    meals_collection = db['meals']

    # Test the connection
    client.admin.command('ping')
    print("Connected to MongoDB!")

    # Insert or update meals
    for meal in meals:
        meals_collection.update_one({"name": meal["name"]}, {"$set": meal}, upsert=True)

    # Insert all meals in bulk
    result = meals_collection.insert_many(meals)
    print(f"Inserted {len(result.inserted_ids)} meals successfully!")
except ConnectionFailure as e:
    print("Failed to connect to MongoDB:", e)
finally:
    client.close()
'''


try:
    # Connect to TinyDB using a JSON file as your database
    db = TinyDB('glo_eat_app.json')
    meals_table = db.table('meals')
    
    print("Connected to TinyDB!")
    
    # Upsert each meal: update the document if one with the same name exists; otherwise, insert it.
    for meal in meals:
        meals_table.upsert(meal, Query().name == meal["name"])
    
    # Alternatively, if you want to insert all meals in bulk (beware of duplicates if upsert was used above):
    # result = meals_table.insert_multiple(meals)
    # print(f"Inserted {len(result)} meals successfully!")
    
except Exception as e:
    print("Failed to perform TinyDB operations:", e)
finally:
    db.close()


