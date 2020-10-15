numero = int(input("Ingresa un numero: "))
while numero != 1:
    if numero % 2 == 0:
        print("%d," % (numero), end = "")
        numero = numero / 2
    else:
        print("%d," % (numero), end = "")
        numero = (numero * 3) + 1
    if numero == 1:
        print("1")