guests = ["Michael Jackson", "Emma P.", "Demtrius Damascus Bartholomewson Johnathan the VII"]

invitation4 = ", welcome to an exclusive dinner with me! Again."

del guests[0]
# Michael Jackson Replacement
guests.insert(1, "Bart S.")

# New guests
guests.append("Evelyn J.")
guests.insert(0, "Livvy Dunne")
guests.insert (4, "Kai Cenat")

# Removing guests
removal = ", I'm sorry to have removed you, maybe another time."
print(guests[0] + removal + "\n")
guests.pop(0)

print(guests[1] + removal + "\n")
guests.pop(1)

print(guests[3] + removal + "\n")
guests.pop(3)

print(guests[2] + removal + "\n")
guests.pop(2)

print("Hey! Today is your lucky day, "+ guests[0] + invitation4 + "\n")
print("Hey! Today is your lucky day, "+ guests[1] + invitation4 + "\n")

del guests[1]
# del guests[2]
del guests[0]
print(guests)