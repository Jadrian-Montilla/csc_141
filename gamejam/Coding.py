from pathlib import Path
import random
from playsound import playsound # type: ignore

filename = ()

playsound(filename)

 # By: Jadrian & Joshua
def get_word():
    wordlist = []
    with open("Coding_Jam/words.txt", 'r') as file:
        wordlist = file.read().split("\n")
    word = random.choice(wordlist)
    return word.lower()

def get_letters(word):
    letters = []
    temp = '_' * len(word)
    if word == " ":
        word.replace(" ", "")
    
    for char in list(word):
        if char not in letters:
            letters.append(char)
    character = " "

    for num, char in enumerate(list(word)):
        if char == character:
            templist = list(temp)
            templist[num] = char
            temp = ''.join(templist)
    return temp

def draw_man(chances):
    if chances == 6:
        print("\n  __")
        print(" /  |")
        print("|   |")
        print("|   ")
        print("|   ")
        print("|   ")
        print("_ _ _ _ _")
    elif chances == 5:
        print("  __")
        print(" /  |")
        print("|   |")
        print("|   o")
        print("|   ")
        print("|   ")
        print("_ _ _ _ _")
    elif chances == 4:
        print("  __")
        print(" /  |")
        print("|   |")
        print("|   o")
        print("|   |")
        print("|   ")
        print("_ _ _ _ _")
    elif chances == 3:
        print("  __")
        print(" /  |")
        print("|   |")
        print("|  \o")
        print("|   |")
        print("|   ")
        print("_ _ _ _ _")
    elif chances == 2:
        print("  __")
        print(" /  |")
        print("|   |")
        print("|  \o/")
        print("|   |")
        print("|   ")
        print("_ _ _ _ _")
    elif chances == 1:
        print("  __")
        print(" /  |")
        print("|   |")
        print("|  \o/")
        print("|   |")
        print("|  |")
        print("_ _ _ _ _")
    elif chances == 0:
        print("  __")
        print(" /  |")
        print("|   |")
        print("|  \o/")
        print("|   |")
        print("|  | |")
        print("_ _ _ _ _")

def start_game():
    word = get_word()
    temp = get_letters(word)
    chances = 6
    found = False
    draw_man(chances)
    active = True
    while active:
        if chances == 0:
            print("Game over\nWord: "+(word.title()))
            break

        print("\n=== Guess the word ===")
        print(temp, end='')
        print("\nLength = " + str(len(temp)))
        print("\nGuesses: "+ str(chances))
        character = input("Enter letter: ")
        guessed = []
        if len(character) == 1 and character.isalpha():
            for num, char in enumerate(list(word)):
                if char == character:
                    templist = list(temp)
                    templist[num] = char
                    temp = ''.join(templist)
                    found = True
                    guessed.append(character)
                elif character == guessed:
                    print("You already entered :" + guessed)
        else:
            print("Only one letter at a time.")
            continue
        if found== True:
            found = False
        else:
            chances -= 1
        if '_' not in temp:
            print("\nWinner! \nWord is: " + word.title())
            if 6 - chances == 0:
                print("First try!")
            else:
                print("Tries: " + str(6 - chances))
            break
        else:
            draw_man(chances)
        print()
        if character == "quit":
            active = False

while True:
    entry = input("Welcome user, would you like to play Hangman? Yes/No ")
    if "Yes" in entry.title():
        start_game()
    elif 'No' in entry.title():
        print("Goodbye.")
        break
    else:
        print("Invalid entry.")
    
    print("\n")