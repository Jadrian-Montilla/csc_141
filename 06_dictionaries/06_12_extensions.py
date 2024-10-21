favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
friends = {
    "Wenda": {
        "numberz": ["214", "123", "529"]
    }
}
for name, lang in favorite_languages.items():
    print(name.title()+ "'s fav coding language is: " +lang.title())

for name, num in friends.items():
    print("\n")
    print (name+" loveessssss these numbers!")
    for word in num.values():
        print(word)
        if lang not in friends.items():
            print("But...")
            print(name + " does not have coding experience...")
        else:
            print("Woah, they love "+ lang)