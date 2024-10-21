prompt = "\nWelcome to the Movie theatre, how old are you?"
prompt += "(\nEnter 'quit' to end program) "

while True:
    age = input(prompt)
    
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            age = str(age)
            print("If you are " + age + " years old, the tickets are free")
        elif age < 13: 
            age = str(age)
            print("If you are " + age + " years old, the tickets cost $10")
        else: 
            age = str(age)
            print("If you are " + age + " years old, the tickets cost $15")