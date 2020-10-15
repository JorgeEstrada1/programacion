numero = int(input("n: "))
suma= 0
for numero in range(1,numero+1):
    if numero % 2 ==0:
        signo= -1
    else:
        signo = 1
    valor = signo / (1+2*(numero-1))
    suma= suma + valor
pi = 4*suma
print(pi)