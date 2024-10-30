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

print(restaurant.name)
print(restaurant.food)

restaurant.describe_restaurant()

restaurant.open_restaurant()
