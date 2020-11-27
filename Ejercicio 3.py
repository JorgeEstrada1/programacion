import random
numeros_correcto=[]
array=[]
tamaño=int(input("ingrese el tamaño de su array: "))
for i in range(0,tamaño):
    num= random.randint(0,300)
    array.append(num)
    num=str(num)
    for i in range(0,tamaño):
        ultimo_digito= num[len(num)-1]
    if ultimo_digito=="5":
        numeros_correcto.append(num)

print(numeros_correcto)
print(array)