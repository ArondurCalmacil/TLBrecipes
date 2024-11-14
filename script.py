import recipes  

def find_recipes_by_ingredients(user_ingredients, recipes_list):
    matching_recipes = []
    user_ingredients = [ingredient.lower() for ingredient in user_ingredients]
    for recipe in recipes_list:
        # Check if every ingredient in the recipe is found in the user's ingredients list
        if any(user_ingredient in ingredient.lower() for user_ingredient in user_ingredients for ingredient in recipe["ingredients"]):
            matching_recipes.append(recipe)
    return matching_recipes

def get_user_ingredients():
    # Get the user's ingredients from input, separated by commas
    user_input = input("Enter the ingredients you have at home, separated by commas: ")
    return [ingredient.strip().lower() for ingredient in user_input.split(",")]

def display_recipes(recipes):
    # Display the recipes or a message if no matching recipes are found
    if not recipes:
        print("Sorry, no recipes match your ingredients.")
        return
    
    for recipe in recipes:
        print(f"\nRecipe: {recipe['name']}")
        print("Ingredients:")
        for ingredient in recipe["ingredients"]:
            print(f"- {ingredient}")
        print(f"Instructions: {recipe['instructions']}\n")

def main():
    # Get user input for ingredients
    user_ingredients = get_user_ingredients()
    
    # Debugging: Show the list of ingredients the user entered
    print(f"User ingredients: {user_ingredients}")
    
    # Get matching recipes from the recipes list
    matching_recipes = find_recipes_by_ingredients(user_ingredients, recipes.recipes)
    
    # Debugging: Show matching recipes (if any)
    print(f"\nMatching recipes: {matching_recipes}")  # Check if the list is populated
    
    # Display the matching recipes
    display_recipes(matching_recipes)

if __name__ == "__main__":
    main()
