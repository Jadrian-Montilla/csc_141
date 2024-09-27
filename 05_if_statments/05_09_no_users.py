Usernames = ["Elizabeth", "Marley", "Admin", "Nova", "Phil"]

del Usernames[0]
del Usernames[0]
del Usernames[0]
del Usernames[0]
del Usernames[0]
if Usernames:
    for user in Usernames:
        if user == "Admin":
            print("\nHello "+user+", would you like to see a status report?")
        else:
            print("\nHello "+user+", thank you for logging in")
else:
    print("We need to find some users")
