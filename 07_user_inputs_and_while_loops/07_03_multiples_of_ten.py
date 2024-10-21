number = input("Give me a number: ")
number = int(number)

if number % 10 == 0:
    print("This number, " + str(number) + " is a multiple of 10")
else:
    print("This number isn't a multiple of 10, do try again.")