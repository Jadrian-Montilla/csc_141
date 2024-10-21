prompt = "\nWhat kind of toppings do you want on your pizza?"
prompt += "\n(Enter 'quit' to finish.) "

while True:
    Man = input(prompt)
    
    if Man == 'quit':
        break
    else:
        print("Adding " + Man)