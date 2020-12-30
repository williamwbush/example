def sand_builder(*toppings):
    """prints a list of sandwich toppings"""
    print("Your sandwich includes: ")
    for topping in toppings:
        print("\t" + "- " + topping)
    print("\n")


sand_builder("bacon", "lettuce", "tomato", "mayonnaise")

sand_builder("ham")

sand_builder("eggs", "bacon")

