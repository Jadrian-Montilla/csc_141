#1, lobsters
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.food = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} has many {self.food}")
        print("This restaurant is also home to lobsters")
    
    def open_restaurant(self):
        print(f"{self.name} is now open")

restaurant = Restaurant("Michael's hotdogs", "hotdogs")

restaurant.describe_restaurant()

print("\n")

restaurant2 = Restaurant("Johnny's maple pancakes", "giant pancakes")

restaurant2.describe_restaurant()

print("\n")

restaurant3 = Restaurant("Olivia's coconut shakes", "milkshakes")

restaurant3.describe_restaurant()