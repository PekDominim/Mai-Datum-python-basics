import random

a=random.randint(1,3)
b = int(input("A gép gondolni egy egész számra 1 és 3 között "))
if a == b:
    print(f"Eltaláltad a gondolt szám {a} volt")
else:
    print(f"Ez sajnos nem sikerült a gondolt szám {a} volt")