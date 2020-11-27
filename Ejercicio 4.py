b=int(input("Ingrese el numero capicua: "))
num_s = str(b)
if num_s == num_s[::-1]:
    print(b, "Es un numero capicua")
else:
    print(b, "No es un numero capicua")
