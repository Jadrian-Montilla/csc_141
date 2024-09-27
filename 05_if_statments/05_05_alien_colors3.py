Alien_color = ["Green", "Red", "Yellow"]
if "Green" in Alien_color:
    print("5 points gained")
    Alien_color.pop(0)
elif "Yellow" in Alien_color:
    print("10 points gained")
else:
    print("15 points gained")

if "Green" in Alien_color:
    print("5 points gained")
elif "Yellow" in Alien_color:
    print("10 points gained")
    Alien_color.pop(1)
else:
    print("15 points gained")

if "Green" in Alien_color:
    print("5 points gained")
elif "Yellow" in Alien_color:
    print("10 points gained")
else:
    print("15 points gained")