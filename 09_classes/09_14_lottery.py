#6 It was pretty hard to understand
from random import choice
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "A", "E", "P", "J", "M"]
chosen=0
winning_card= []
while chosen!=4:
    digit= (choice(digits))
    chosen+=1
    winning_card.append(digit)
print(f"IF your ticket matches the following: ({winning_card}), you win!\n")
# lottery1 = choice(digits)
# lottery2 = choice(digits)
# lottery3 = choice(digits)
# lottery4 = choice(digits)
# print(f"IF your ticket matches the following: {lottery1}{lottery2}{lottery3}{lottery4}\nYou win!")