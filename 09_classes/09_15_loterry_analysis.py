#2
from random import choice
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "A", "E", "P", "J", "M"]
chosen=0
winning_card= []
while chosen!=4:
    digit= (choice(digits))
    chosen+=1
    winning_card.append(digit)
print(f"IF your ticket matches the following: ({winning_card}), you win!\n")

my_ticket = [2, "E", 8, "P"]
print(str(my_ticket))
print(str(winning_card))
if my_ticket == winning_card:
    print("YOU WON")
else:
    print("Try again another time.")