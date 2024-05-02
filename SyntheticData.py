import csv
import os
from config_reader import fetch_config_dict

def save_recipes_to_csv(recipes, filename):
    fieldnames = ['recipe_id','Name', 'Image URL', 'Ingredients', 'Instructions', 'Tags', "description", "prep_time", "cook_time", "total_time", "servings", "calories", 'Valid Ingredients']
    file_path = os.path.expanduser("~/Desktop/" + filename)
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for recipe in recipes:
            writer.writerow(recipe)

# Only one I didnt know is Test case 33, not sure how we will achieve

recipes = [
    {
        # Test cases 1, 2
        "recipe_id" : 1,
        'Name': "Chicken and Rice",
        'Image URL': "https://d2t88cihvgacbj.cloudfront.net/manage/wp-content/uploads/2013/10/homemade-teriyaki-2.jpg?x29814",
        'Ingredients': "chicken,rice,chicken stock,oil,salt,black pepper",
        'Instructions': "1. Cook rice in rice cooker. 2. In a separate pan, fry chicken with the oil, salt and pepper until crispy. 3. When rice finished, add onto one plate and serve immediately.",
        'Tags': "Healthy,Protein",
        "description" : "",
        "prep_time": 15,
        "cook_time": 30,
        "total_time": 45,
        "servings": 4,
        "calories": 300,
        'Valid Ingredients': "chicken,rice,salt,black pepper"
        
    },
    {
        # Test cases 18, 22
        "recipe_id" : 2,
        'Name': "Summer Salad",
        'Image URL': "https://healthyfitnessmeals.com/wp-content/uploads/2020/05/Strawberry-chicken-salad-9.jpg",
        'Ingredients': "romaine lettuce,crouton,balsamic dressing,strawberry, chicken",
        'Instructions': "1. Wash and chop romaine lettuce. 2. In a separate pan, fry chicken with the oil, salt and pepper until crispy. 3. Toss lettuce with croutons, strawberries, and balsamic dressing. 3. Add chiecken on top and serve chilled.",
        'Tags': "Salad,Fruit,Meat,Vegetables",
        "description" : "",
        "prep_time": 15,
        "cook_time": 30,
        "total_time": 45,
        "servings": 4,
        "calories": 300,
        'Valid Ingredients': "romaine lettuce,croutons,chicken,strawberry"
    },
    {
        # Test cases 3
        "recipe_id" : 3,
        'Name': "Spaghetti with Tomato Sauce",
        'Image URL': "https://www.allrecipes.com/thmb/iZmE8xvusvYu16RIMZLdG1HX3OM=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/254517-spaghetti-sauce-with-fresh-tomatoes-3x2-79-609ce4edcafb4191b609180163fed92b.jpg",
        'Ingredients': "spaghetti,tomato,parmesan cheese,garlice,salt,black pepper",
        'Instructions': "1. Cook spaghetti according to package instructions. 2. In a separate pan, crush tomatoes and add the garlic, salt and pepper, let simmer for 30 min. 3. When pasta ready, drain spaghetti and mix with tomato sauce. 4. Grate the parmesan on top, and serve immediately.",
        'Tags': "Italian,Vegetarian",
        "description" : "",
        "prep_time": 15,
        "cook_time": 30,
        "total_time": 45,
        "servings": 4,
        "calories": 300,
        'Valid Ingredients': "spaghetti,tomato,garlic,parmesan cheese,salt,black pepper"        
    },
    {
        # Test cases 4
        "recipe_id" : 4,
        'Name': "Jalapeño Poppers",
        'Image URL': "https://cookieandkate.com/images/2018/09/baconless-jalapeno-poppers-recipe.jpg",
        'Ingredients': "jalapeño,cream cheese,oil",
        'Instructions': "1. Prepare jalapeño by removing stem and seeds. 2. Stuff jalapeño with the cream chesse and add to lightly oiled pan in 350 degree oven 3. Pull out of oven after 30 min, and let cool for 5 before serving. ",
        'Tags': "American",
        "description" : "",
        "prep_time": 15,
        "cook_time": 30,
        "total_time": 45,
        "servings": 4,
        "calories": 300,
        'Valid Ingredients': "jalapeño,cream cheese"        
    },
    {
        # Test cases 7, 12, 16, 19, 21, 23, 24, 25, 26, 28, 29, 30, 35
        "recipe_id" : 5,
        'Name': "Spaghetti with Tomato Sauce and Chicken",
        'Image URL': "https://outgrilling.com/wp-content/uploads/2022/10/Grilled-Chicken-Spaghetti-Recipe-photo.jpg",
        'Ingredients': "pasta,tomato,parmesan cheese,garlice,oil,salt,black pepper",
        'Instructions': "1. Cook spaghetti according to package instructions. 2. In a separate pan, crush tomatoes and add the garlic, salt and pepper, let simmer for 30 min. 3. 2. In another pan, fry chicken with the oil, salt and pepper until crispy. 4. When pasta ready, drain spaghetti and mix with tomato sauce. 4. Slice chicken and grate the parmesan on top, and serve immediately.",
        'Tags': "Italian",
        "description" : "",
        "prep_time": 15,
        "cook_time": 30,
        "total_time": 45,
        "servings": 4,
        "calories": 300,
        'Valid Ingredients': "pasta,tomato,chicken,garlic,parmesan cheese,salt,black pepper"        
    },
    {
        # Test cases 8, 10, 34
        "recipe_id" : 6,
        'Name': "Carmelized Peaches",
        'Image URL': "https://www.pumpkinnspice.com/wp-content/uploads/2016/06/grilled-peaches-cinnamon-brown-sugar-5-1024x683.jpg",
        'Ingredients': "peach,sugar",
        'Instructions': "1. Wash and slice peach. 2. Pour sugar on plate, and dip one side of the peach in sugar 3. Add peach sugar side down to a pan and let camrelize. 4. After sugar melted, let cool for 2 min and serve.",
        'Tags': "Vegetarian,Vegan,Dessert,Gluten-free",
        "description" : "",
        "prep_time": 15,
        "cook_time": 30,
        "total_time": 45,
        "servings": 4,
        "calories": 300,
        'Valid Ingredients': "sugar,peach"
    },
    {
        # Test cases 14
        "recipe_id" : 7,
        'Name': "Loaded Vegetable Pasta",
        'Image URL': "https://familystylefood.com/wp-content/uploads/2023/10/Roasted-Vegetable-Pasta-bowl.jpg",
        'Ingredients': "penne pasta,tomato,bell pepper,zucchini,mushroom,red onion,spinach,oil,garlic,salt,black pepper,parmesan cheese",
        'Instructions': "1. Cook penne pasta according to package instructions. 2. In a large skillet, heat olive oil over medium heat. 3. Add minced garlic and diced red onion, sauté until fragrant. 4. Add sliced bell pepper, diced zucchini, sliced mushrooms, and halved cherry tomatoes to the skillet. Cook until vegetables are tender. 5. Season with salt and black pepper to taste. 6. Toss cooked pasta and fresh spinach with the vegetable mixture. 7. Serve hot, garnished with grated parmesan cheese.",
        'Tags': "Vegetarian,Healthy",
        "description" : "",
        "prep_time": 15,
        "cook_time": 30,
        "total_time": 45,
        "servings": 4,
        "calories": 300,
        'Valid Ingredients': "penne pasta,tomato,bell pepper,zucchini,mushroom,red onion,spinach,oil,garlic,salt,black pepper,parmesan cheese"
    },
    {
        # Test cases 15, 31
        "recipe_id" : 8,
        'Name': "Million Dollar Pasta",
        'Image URL': "https://www.sprinklesandsprouts.com/wp-content/uploads/2018/11/Black-Truffle-PastaSQ.jpg",
        'Ingredients': "pasta,heavy cream,parmesan cheese,truffle,salt,black pepper",
        'Instructions': "1. Cook pasta according to package instructions. 2. In a saucepan, heat heavy cream over medium heat and add parmesan cheese into the cream and stir until melted and smooth. 3. Toss cooked pasta with the truffle cream sauce until well coated. 4. Serve hot, garnished with additional shaved truffles if desired.",
        'Tags': "Luxury,Truffle,Pasta",
        "description" : "",
        "prep_time": 15,
        "cook_time": 30,
        "total_time": 45,
        "servings": 4,
        "calories": 300,
        'Valid Ingredients': "pasta,heavy cream,parmesan cheese,truffles,salt,black pepper"
    },
    {
        # Test cases 36
        "recipe_id" : 9,
        'Name': "Simple Grilled Chicken",
        'Image URL': "https://www.simplyrecipes.com/thmb/mZq-tAKO98F0KUZOsohbXlo37s8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Grilled-Chicken-LEAD-SEO-Vertical-3c66b6ae87184189920ad84f3f1db6bb.jpg",
        'Ingredients': "chicken,lemon,olive oil",
        'Instructions': "1. Preheat grill to medium-high heat. 2. Season chicken breasts with salt and pepper. 3. Drizzle olive oil over chicken breasts and squeeze fresh lemon juice on top. 4. Place chicken breasts on the grill and cook for 6-8 minutes on each side, or until fully cooked through. 5. Remove from grill and let rest for a few minutes before serving.",
        'Tags': "Grilled Chicken,Healthy",
        "description" : "",
        "prep_time": 15,
        "cook_time": 30,
        "total_time": 45,
        "servings": 4,
        "calories": 300,
        'Valid Ingredients': "chicken breasts,lemon,olive oil"
    }


]

config_dict = fetch_config_dict()
save_recipes_to_csv(recipes, config_dict.get('recipe_csv', 'SyntheticRecipes.csv'))
