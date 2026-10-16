"""docstring module"""
def main():
    """main function"""
    valid_ingredients = {
        "Pad Thai Sauce",
        "Tofu",
        "Pickle Turnip",
        "Shrimp",
        "Bean Sprouts",
        "Noodle",
        "Chives",
        "Lime",
        "Egg",
        "Oil",
        "Peanuts"
    }
    valid_tastes = {"Sweet", "Sour", "Salty"}
    used_ingredients = set()
    while True:
        item = input().strip()
        if item == "Cook":
            break
        if item:
            used_ingredients.add(item)
    tastes = set()
    while True:
        taste = input().strip()
        if taste == "End":
            break
        if taste:
            tastes.add(taste)
    if not used_ingredients.issubset(valid_ingredients):
        print("This is not Pad Thai!!!")
    elif used_ingredients != valid_ingredients:
        print("This is bad!")
    elif tastes == valid_tastes:
        print("Delicious!")
    else:
        print("Not Bad...")
main()
