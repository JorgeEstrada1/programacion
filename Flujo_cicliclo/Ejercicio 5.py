triangulo = int(input("Indique un numero: "))
for i in range (triangulo + 1):
    for j in range (i):
        print("*", end="")
    print()