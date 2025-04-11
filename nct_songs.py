import random

# Read songs from file
with open('nct_songs.txt', 'r') as file:
    nct_songs = [line.strip() for line in file]

# Randomize and print
print("Your random NCT song is:", random.choice(nct_songs))

print("Such a good choice!"))
