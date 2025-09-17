number = int(input("Add meg az évet: "))

if (number % 4 == 0 and number % 100 != 0) or (number % 400 == 0):
    print("szökőév")
else:
    print("Nem szökőév 🙄")