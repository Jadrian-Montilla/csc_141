prompt = "\nWhat kind of toppings do you want on your pizza?"
prompt += "\n(Enter 'quit' to finish.) "

letter = 1
while letter <= 25:
    print(letter)
    letter += 1


active = True
while active:
    Message = input("Oooooo I'm a ghoooost!!! I can seeeee youuuuu!!!(y/n) ")
    if Message == 'n':
        print("Oh......")
        active = False
    else:
        Message = print("Haha! You will feel my wrath!")
        active = False

Man = ""
while Man != 'quit':
    Man = input(prompt)
    
    if Man == 'quit':
        break
    else:
        print("Adding " + Man)