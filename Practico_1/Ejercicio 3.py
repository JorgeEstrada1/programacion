dividendo = int(input("Escriba el dividendo: "))
divisor = int(input("Escriba el divisor: "))
if dividendo % divisor == 0:
    print(f"La division es exacta. cociente: {dividendo//divisor} resto: {dividendo%divisor}")
else:
    print(f"La division no es exacta. Cociente: {dividendo//divisor} resto: {dividendo%divisor}")


