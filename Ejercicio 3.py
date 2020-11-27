import random
numero=[]
array=[]
tamaño=int(input("ingrese el tamaño de su array: "))
digito=input("ingrese el ultimo digito para verificar: ")
for i in range(0,tamaño):
    num= random.randint(0,300)
    array.append(num)
    num=str(num)
    for i in range(0,tamaño):
        ultimo_digito= num[len(num)-1]
    if ultimo_digito==digito:
        numero.append(num)

print(numero)
print(array)