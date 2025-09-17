v4 = int(input("Adj meg első számot: " ))
v5 = int(input("Adj meg második számot: " ))
v6 = int(input("Adj meg harmadik számot: " ))

if v4 > v5 and v5 > v6:
    print(v4)
elif v5>v4 and v5>v6:
    print(v5)
else:
    print(v6)