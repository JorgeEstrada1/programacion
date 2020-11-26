b=int(input("Ingrese el numero capicua: "))
num_s = str(b)
if num_s == num_s[::-1]:
    print(b, "Es un numero capicua")
    print(num_s[::-1])
else:
    print(b, "No es un numero capicua")
