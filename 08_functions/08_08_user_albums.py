def make_album(name, cover, songs= None):
    song_maker = {"Artist": name.title(), "Album": cover.title()}
    if songs:
        song_maker['Number of songs'] = songs
    return song_maker

while True:
    print("\nEnter artist and album name")
    print("(Enter 'q' to stop)")

    musician = input("Artist: ")
    if musician == 'q':
        break

    album = input("Album: ")
    if album == 'q':
        break

music_maker = make_album(musician, album)
print(music_maker)