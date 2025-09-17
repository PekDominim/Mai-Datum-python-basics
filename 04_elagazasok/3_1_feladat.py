import random

thinked_number = int((random.randint(1, 5)))

player_number = int(input("Adj meg egy számoot 1 és 5 között! "))

if player_number == thinked_number:
    print("Eltaláltad")
elif player_number > thinked_number:
    print ("Majdnem, ez több lett")
elif player_number < thinked_number:
    print("Majdnem, ez kevesebb lett")
