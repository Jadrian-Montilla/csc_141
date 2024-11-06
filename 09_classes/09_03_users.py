# 2, thinking of the attibutes to put in was tough
class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.place = location
        self.work = occupation
    
    def describe_user(self):
        print(f"{self.fname} likes to eat lobsters and solve puzzles.")
    
    def greet_user(self):
        print(f"Hello! I am {self.fname} {self.lname}, pleased to meet you!")

person1 = User("Kenny", "Marage", 25, "TX", "CEO of Lobster Manufacturer")

print(person1.fname+ "\n"+ person1.lname+ "\n"+ str(person1.age)+ "\n"+ 
      person1.place+ "\n"+ person1.work)
person1.describe_user()

person1.greet_user()
print("\n")

person2 = User("Jace", "Willu", 17, "UK", "Cashier")
print(person2.fname+ "\n"+ person2.lname+ "\n"+ str(person2.age)+ "\n"+ 
      person2.place+ "\n"+ person2.work)

person2.describe_user()

person2.greet_user()
print("\n")

person3 = User("Carter", "Hamburr", 22, "Bronx", "Unemployed")

print(person3.fname+ "\n"+ person3.lname+ "\n"+ str(person3.age)+ "\n"+ 
      person3.place+ "\n"+ person3.work)
person3.describe_user()

person3.greet_user()
print("\n")

person4 = User("Nicole", "Manderin", 32, "EU", "Manager of Olivia's coconut shakes")
print(person4.fname+ "\n"+ person4.lname+ "\n"+ str(person4.age)+ "\n"+ 
      person4.place+ "\n"+ person4.work)

person4.describe_user()

person4.greet_user()