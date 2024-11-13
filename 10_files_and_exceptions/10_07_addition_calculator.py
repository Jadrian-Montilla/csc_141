#
print("Give me two numbers (enter q to stop)")
while True:
    number1 = input("Insert first number: ")
    if number1 == 'q':
        break
    
    number2 = input("Insert second number: ")
    if number2 == 'q':
        break

    try:
        print(int(number1) + int(number2))
    except ValueError:
        print("You can't add letters!")