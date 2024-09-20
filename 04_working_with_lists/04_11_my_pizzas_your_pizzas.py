pizzas = ["Pepperoni", "Cheese", "Ham"]
friends_pizza = pizzas[:]

pizzas.append("Black Olives")
friends_pizza.append("Beef")
print("My favorite pizzas are: ")
for p in pizzas:
    print(p)
print("\nMy friend's favorite pizzas are: ")
for friend in friends_pizza:
    print(friend)