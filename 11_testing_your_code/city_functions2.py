def city_country(city, country, population=None):
    if population:
        area = f"{city}, {country} - population ={str(population)}"
    else:
        area = f"{city}, {country}"
    return area.title()
#2