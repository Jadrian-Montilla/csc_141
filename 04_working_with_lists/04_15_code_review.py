pizzas = ["Pepperoni",
        "Cheese",
        "Ham"]
for P in pizzas:
    print("me loves " + P)
print("I love these 3 pizzas \nIt's hard for me to eat due to braces", 
    "\nbut i really love pizza")


Objects = ["Lamp", "Wardrobe", "Pen", "Pocket Watch", "Shoes", 
           "Gloves", "Bed", "Lightbulb", "Case", "Glasses"]
print("\nFirst three are ")
print(Objects[0:3])

print("\nMiddle three are ")
print(Objects[4:7])

print("\nLast three are ")
print(Objects[-3:])

Cube = []
for cubed in range(1,11):
    Cube.append(cubed**3)
    print(Cube)