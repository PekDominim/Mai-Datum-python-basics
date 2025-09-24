folytatja = True
while folytatja:
    print("Vidd ki a szemetet!")
    valasz = input("Mondjam meg egyszer? (i/n) ")
    if valasz == "n":
        folytatja = False
    elif valasz == "nem":
        print("i vagy n betűt használj")
print(">> Program vége! <<")