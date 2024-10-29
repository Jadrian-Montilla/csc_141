def create_sandwich(*toppings):
    print(f"\nadding these to your sandwich:")
    for food in toppings:
        print(f"- {food}")

create_sandwich("ham", "cheese")
create_sandwich("bacon", "anchovis", "eggs")
create_sandwich("pickles", "beef", "cheese")