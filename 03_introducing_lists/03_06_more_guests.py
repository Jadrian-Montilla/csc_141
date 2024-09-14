guests = ["Michael Jackson", "Emma P.", "Demtrius Damascus Bartholomewson Johnathan the VII"]

invitation3 = ", I welcome you to a big and cool and awesome dinner table. PLEASE ARRIVE."

del guests[0]
# Michael Jackson Replacement
guests.insert(1, "Bart S.")

# New guests
guests.append("Evelyn J.")
guests.insert(0, "Livvy Dunne")
guests.insert (4, "Kai Cenat")

print("Hello for the third time " + guests[1] + invitation3 + "\n")
print("Hello for the third time " + guests[3] + invitation3 + "\n")
print("Hello for the second time " + guests[2] + invitation3 + "\n")
print("Hello " + guests[0] + invitation3 + "\n")
print("Hello " + guests[4] + invitation3 + "\n")
print("Hello " + guests[5] + invitation3 + "\n")

print("Sorry my unfortunate guests, it seems the table will arrive never so I must only bring 2 people.")