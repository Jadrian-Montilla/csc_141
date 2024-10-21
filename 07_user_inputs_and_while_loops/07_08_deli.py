sandwich_orders = [
    "Ham Sandwich", 
    "Bacon, Egg, and Cheese Sandwich", 
    "Pickled Ham Sandwich",
    "Sausage Ham Sandwich",
    "Guacamole, Onion, and Egg Sandwich"
    ]
finished_sandwiches = []

while sandwich_orders:
    made_orders = sandwich_orders.pop()

    print("\nI have finished your " + made_orders)
    finished_sandwiches.append(made_orders)

print("\nHere are all the sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)