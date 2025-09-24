import random

a = random.randint(1,2)

choice = input("fej vagy írás ")


if a == 1 and choice == "fej":
    print("fej eltaláltad")
elif a == 2 and choice == "írás":
    print("írás eltaláltad")
else:
    print("nem talált")