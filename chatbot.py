import time
import random
import os

os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(2)

name = input("PyBot: Hi, Im PyBot! What is your name? Your Name: ")

time.sleep(2)
print("PyBot: Hi " + name)

feeling = input("PyBot: How are you feeling right now? Your Mood: ")
time.sleep(2)

time.sleep(2)
if "good" in feeling.lower():
    print("PyBot: I'm feeling good too!")
elif "awesome" in feeling:
    print("PyBot: Thats Amazing!")
else:
    print("PyBot: I'm sorry to hear that!")

time.sleep(2)
favcolour = input("PyBot: What is your favourite colour? Your Colour: ")

colours = ["Red", "Green", "Blue", "Black", "Pink", "Purple", "Orange", "Yellow", "White", "All Colours"]

time.sleep(2)
print("PyBot: My favourite colour is " + random.choice(colours))

favshows = ["South Park", "Stranger Things", "Family Guy", "Young Sheldon", "The Good Doctor", "Spongebob", "Any Shows"]

favshow = input("PyBot: What is your favourite show? Your Show: ")
time.sleep(2)
print("PyBot: I like " + random.choice(favshows))
time.sleep(2)
favmusic = ["Metal", "Grunge", "Rock", "Pop", "Rap", "Country", "Folk", "Instrumental", "Phonk", "Acapella", "Any Genre"]

favmusicq = input("PyBot: What is your favourite music genre? Your Genre: ")
time.sleep(2)
print("PyBot: I personally like " + random.choice(favmusic) + ". Its good and I reccomend you give some of them artists or bands a listen!")
time.sleep(2)

futurent = input("PyBot: Do you ever wonder what the future will look like? Your Answer: ")
time.sleep(2)
print("PyBot: I do sometimes. Its really interesting.")
time.sleep(2)

opiniononcrypto = input("PyBot: Do you think cryptocurrency is good? I think its half good and half bad. What about you? Your Answer: ")
time.sleep(2)

print("PyBot: I have to go now, Goodbye. \n Coded By Wyn.")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')