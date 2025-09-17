temp = int(input("Add meg a hőmérsékletet Celsiusban: "))

if temp < 0:
    print("Nagyon hideg, öltözz melegen!")
elif 0 <= temp <= 20:
    print("Hűvös, kabát ajánlott.")
elif 21 <= temp <= 30:
    print("Kellemes idő.")
else:
    print("Forróság, igyál sok vizet!")