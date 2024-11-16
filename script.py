import requests  

API_HOST = "the-cocktail-db.p.rapidapi.com"  
API_KEY = "540b011b8fmshbd4250a8cc9bba9p146cbdjsn9edcab48a0f8"  

def getInput():
    print("Enter:\n1: Filter by Cocktail Name\n2: Filter by Ingredient")
    choice = input("Select 1 or 2: ").strip()

    if choice == "1":
        name = input("Enter the cocktail name: ").strip()
        return {"type": "name", "value": name}
    elif choice == "2":
        ingredients = input ("Enter the list of ingredients (seperated by a comma): ").strip()
        return {"type": "ingredients", "value": ingredients}

def filterByName(name):
    url = f"https://{API_HOST}/search.php"
    headers = {"x-rapidapi-host": API_HOST, "x-rapidapi-key": API_KEY}
    params = {"s": name}

    response = requests.get(url, headers=headers, params=params)  
    if response.status_code == 200:  
        return response.json().get("drinks", []) 

def filterByIngredient(ingredients):
    url = f"https://{API_HOST}/filter.php"
    headers = {"x-rapidapi-host": API_HOST, "x-rapidapi-key": API_KEY}
    ingredientsList = [ingredient.strip() for ingredient in ingredients.split(",") if ingredient.strip()]  
    params = {"i": ",".join(ingredientsList)}  

    response = requests.get(url, headers=headers, params=params)  
    if response.status_code == 200:  
        return response.json().get("drinks", []) 

def getCocktailDetails(name):  
    url = f"https://{API_HOST}/search.php"  
    headers = {"x-rapidapi-host": API_HOST, "x-rapidapi-key": API_KEY}  
    params = {"s": name}  

    response = requests.get(url, headers=headers, params=params)  
    if response.status_code == 200:  
        drinks = response.json().get("drinks", [])  
        return drinks[0] if drinks else None  
    return None  

def displayName(cocktails):
    if not cocktails:
        print("No matching cocktails found")
    
    for cocktail in cocktails:
        if cocktail:  
            print("\n---------------------------")  
            print(f"Name: {cocktail.get('strDrink', 'Name not available')}")  

            print("Ingredients:")  
            for i in range(1, 16):  
                ingredient = cocktail.get(f'strIngredient{i}')  
                measure = cocktail.get(f'strMeasure{i}')  
                if ingredient:  
                    print(f"{measure} {ingredient}")  
            
            instructions = cocktail.get('strInstructions', 'Instructions not available.')  
            print(f"Instructions: {instructions}")  
            print("---------------------------\n")  
        else:  
            print(f"Details for {cocktail.get('strDrink')} not found.")  

def displayResult(cocktails):
    if not cocktails:
        print("No matching cocktails found")
    
    for cocktail in cocktails:
        coctailInfo = getCocktailDetails(cocktail.get('strDrink'))  

        if coctailInfo:  
            print("\n---------------------------")  
            print(f"Name: {coctailInfo.get('strDrink', 'Name not available')}")  

            print("Ingredients:")  
            for i in range(1, 16):  
                ingredient = coctailInfo.get(f'strIngredient{i}')  
                measure = coctailInfo.get(f'strMeasure{i}')  
                if ingredient:  
                    print(f"{measure} {ingredient}")  
            
            instructions = coctailInfo.get('strInstructions', 'Instructions not available.')  
            print(f"Instructions: {instructions}")  
            print("---------------------------\n")  
        else:  
            print(f"Details for {cocktail.get('strDrink')} not found.")  

def main():  
    user_input = getInput()  
    if user_input["type"] == "name":  
        cocktails = filterByName(user_input["value"])  
        displayName(cocktails)  
    if user_input["type"] == "ingredients":  
        cocktails = filterByIngredient(user_input["value"])  
        displayResult(cocktails)  

if __name__ == "__main__":  
    main()