sandwich_orders = [
    "Ham Sandwich", 
    "Pastrami",
    "Bacon, Egg, and Cheese Sandwich", 
    "Pickled Ham Sandwich",
    "Pastrami",
    "Pastrami",
    "Sausage Ham Sandwich",
    "Guacamole, Onion, and Egg Sandwich"
    ]

finished_sandwiches = []

print("We've run out of Pastrami")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    made_orders = sandwich_orders.pop()

    print("\nI have finished your " + made_orders)
    finished_sandwiches.append(made_orders)

print("\nHere are all the sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)