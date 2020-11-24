def Fact(numero):
    if numero >= 0:
        factorial = 1

        if numero == 0 or numero == 1:
            factorial = 1
        else:
            for i in range(1, numero + 1):
                factorial *= i

        print(f'{numero}! = {factorial}')
for n in range(1,21):
    Fact(n)


