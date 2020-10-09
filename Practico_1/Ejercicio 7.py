n1 = int(input("Ingrese primer numero: "))
for i in range (1, n1+1):
    resultado = n1 % i
    if resultado == 0:
        print(i)
