favorite_places = {
    "Paula":["great wall of china", "mount everest"],
    "\nKiko":["paris", "italy", "vancouver"],
    "\nAnnabelle":["grand canyon", "egypt", "argentina"]
}
for name, place in favorite_places.items():
    print(name + "'s favorite places are:")
    for area in place:
        print(area.title())