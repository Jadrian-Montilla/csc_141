# 6, it's a bit hard to understand exactly what they want me to do and im not
#  sure if i did the list thing correctly
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.food = cuisine_type
        self.number_served = 20 #0
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, meals):
        self.number_served += meals

    def describe_restaurant(self):
        print(f"{self.name} has many {self.food}")
        print("This restaurant is also home to lobsters")
    
    def open_restaurant(self):
        print(f"{self.name} is now open")
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = ["Vanilla", "Chocolate", "Strawberry", "Pineapple", 
                       "Mango", "Mint", "Cookies and Cream", "Cookie Dough", 
                       "Blueberry"]
    def describe_flavors(self):
        print(f"{self.name} has many different flavors, such as:")
        for taste in self.flavor:
            print(taste)

Icestand = IceCreamStand("Cold Sundays", "Cold desserts")
Icestand.describe_flavors()