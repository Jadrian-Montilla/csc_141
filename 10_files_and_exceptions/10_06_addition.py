#2
print("Give me two numbers")
number1 = input("Insert first number: ")
number2 = input("Insert second number: ")
try:
    print(int(number1) + int(number2))
except ValueError:
    print("You can't add letters!")