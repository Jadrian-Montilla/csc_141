# 1
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

restaurant = Restaurant("Michael's hotdogs", "hotdogs")
restaurant.set_number_served(40)
print(f"{restaurant.number_served} was served yesterday.")
restaurant.increment_number_served(30)
print(f"{restaurant.number_served} was served today.")