def make_album(artist, album_title, tracks=""):
    """Return a custom artist and album dictionary."""
    custom_album = {'artist': artist, 'album': album_title}
    if tracks:
        custom_album["tracks"] = tracks
    return custom_album

# illinoise = make_album("Sufjan Stevens", "Illinoise", 12)
# print(illinoise)
# michigan = make_album("Sufjan Stevens", "Michigan")
# print(michigan)
# seven_swans = make_album("Sufjan Stevens", "Seven Swans", 2)
# print(seven_swans)

while True:
    print("\nEnter the name of an artist.")
    print("Enter 'q' at any time to quit.")
    artist = input("")
    if artist.lower() == "q":
        break
    album = input("Enter their album name. ")
    if album.lower() == "q":
        break
    custom_album = make_album(artist, album)
    print(custom_album)