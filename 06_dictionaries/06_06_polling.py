favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python'
}
friends = ["wenda", "chist", "pentis", "phil", "jen"]
for name in friends:
    print("\nHello, " + name.title())

    if name not in favorite_languages.keys():
        print (name.title() + ", you need to take the poll")
    else:
        print("Thank you for taking the poll")