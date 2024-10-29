def make_car(maker, model, **car_info):
    car_info["manufacturer"] = maker
    car_info["car's model"] = model
    return car_info

car = make_car("Honda", "CR-V", color= "Red", touchscreen= True)

print(car)