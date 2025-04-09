# save_songs.py

print("Type NCT songs (no quotes needed). Type 'done' when you're finished:\n")

with open("nct_songs.txt", "w", encoding="utf-8") as f:
    while True:
        song = input("Add song: ")
        if song.lower() == "done":
            break
        f.write(song + "\n")

print("\n✅ Songs saved to nct_songs.txt!")
