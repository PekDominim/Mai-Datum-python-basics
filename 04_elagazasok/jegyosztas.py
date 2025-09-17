value = int(input("Adj meg egy egész számot: "))
if value % 2 == 0:
    print("páros")
else:
    print("paratlan")

value2 = float(input("Adj meg egy számot: "))
if value2 == 0:
    print("nulla")
elif value < 0:
    print("pozitív")
elif value > 0:
    print("negativ")

value3 = int(input("Adj meg egy szamot 0 és 100 között: "))
if value3 < 0:
    print("🙄")
elif value3 < 50:
    print("Elegtelen")
elif value3 < 65:
    print("elgeseges")
elif Value3 < 80:
   print("Közepes")
elif value3 < 90:
    print("jo")
elif value3 < 101:
    print("jeles")

