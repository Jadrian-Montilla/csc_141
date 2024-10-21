cities = {
    "San_Francisco": {
        "Country":"U.S.",
        "Population":"870,000",
        "Fact":"known for its steep hills and eclectic mix of architecture."
    },
    "Abilene": {
        "Country":"U.S.",
        "Population":"130,000",
        "Fact":"Largest public collection of storybooks"
    },
    "Portland": {
        "Country":"U.S.",
        "Population":"650,000",
        "Fact":"It's approximately 100 miles upriver from the Pacific ocean"
    }
}
for cities, info in cities.items():
    print("City: " + cities)
    details = ("\tLocated in: "+ info["Country"])+ ("\n\tPopulation: "+ info["Population"])+ ("\n\tOne fact: "+ info["Fact"])
    print(details)