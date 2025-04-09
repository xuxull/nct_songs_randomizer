nct_songs = ["Walk", "We go up", "Phantom"]
print(nct_songs[1])

nct_songs.append("Teddy bear")

print(nct_songs)

nct_songs.remove(nct_songs[0])
print(nct_songs)

nct_songs.insert(1, "Misfits")

print("Teddy bear" in nct_songs)