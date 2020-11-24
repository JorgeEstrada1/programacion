v1=[]
v2=[]
for i in range (0,5):
    v1a=int(input("Ingrese un numero: "))
    v1.append(v1a)
for i in range (0,5):
    v2a=int(input("Ingrese un numero: "))
    v2.append(v2a)
vector=[]
for i in range (0,5):
    suma=v2[i]+v1[i]
    vector.append(suma)
print(v1)
print(v2)
print(vector)