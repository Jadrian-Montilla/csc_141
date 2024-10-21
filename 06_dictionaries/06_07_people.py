Person1 = {
    "first_name":"John", 
    "last_name":"Vegetabl", 
    "age":"16", 
    "city":"Yasoinaba"
}

Person2 = {
    "first_name":"Nicolas",
    "last_name":"Egg",
    "age":"16",
    "city":"Iwatodai"
}

Person3 = {
    "first_name":"Ezekiel",
    "last_name":"Skywalkr",
    "age":"16",
    "city":"Shibuya"
}

People = [Person2, Person1, Person3]

for person in People:
    print(person["first_name"])
    print(person["last_name"])
    print(person["age"])
    print(person["city"])
    print("\n") 