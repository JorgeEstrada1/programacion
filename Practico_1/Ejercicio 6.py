num1 = int(input("Ingrese numero: "))
num2 = int(input("Ingrese numero: "))
a = min(num1 , num2)
c = max(num1 , num2)
b = (num1 + num2) - a - c
print(f"{a} {c}")

num1 = int(input("Ingrese numero: "))
num2 = int(input("Ingrese numero: "))
num3 = int(input("Ingrese numero: "))
a = min(num1 , num2 , num3)
c = max(num1 , num2 , num3)
b= (num1 + num2 + num3) - a - c
print(f"{a} {b} {c}")