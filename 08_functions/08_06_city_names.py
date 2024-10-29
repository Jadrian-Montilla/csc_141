def city_country(city, country):
    area = f"\n{city}, {country}"
    return area.title()

place1 = city_country("reading", "united states")
print(place1)
place2 = city_country("quebec", "canada")
print(place2)
place3 = city_country("brisbane", "australia")
print(place3)