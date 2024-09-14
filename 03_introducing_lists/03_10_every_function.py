Animals = ["Sheeps", "Cats", "Dogs", "Rabbits", "Crocodiles", "Ferrets"]

print(Animals)

Animals.sort()
print(Animals)

Animals.insert(3, "Owls")
print(Animals)
print(len(Animals))
print("Animals")

del Animals[1]

print(Animals)

print(sorted(Animals,reverse=True))

Animals.append("Sungazers")
print(Animals)

print("I really love " + Animals[5])

print("But, I don't like " + Animals[2] + " as much")
Animals.pop(2)
print(Animals)

print("I also like reading backwards alphabetically")
Animals.sort(reverse=True)
print(Animals)