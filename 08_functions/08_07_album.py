def make_album(name, cover, songs= None):
    song_maker = {"Artist": name.title(), "Album": cover.title()}
    if songs:
        song_maker['Number of songs'] = songs
    return song_maker

musician1 = make_album("tyler the creator", "igor", 12)
print(musician1)
musician2 = make_album("eminem", "the death of slim shady")
print(musician2)
musician3 = make_album("k'naan", "troubadour")
print(musician3)