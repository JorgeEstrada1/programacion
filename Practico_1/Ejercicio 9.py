operando = float(input("operando: "))
operador = input("operador: ")
operando2 = float(input("operando: "))
suma = "+"
resta = "-"
multi = "*"
division = "/"
resultado_suma = float(operando + operando2)
resultado_resta = float(operando - operando2)
resultado_multi = int(operando * operando2)
resultado_divi = int(operando / operando2)
if operador == suma:
    print(f"{operando} + {operando2} = {resultado_suma}" )
if operador == resta:
    print(f"{operando} - {operando2} = {resultado_resta}")
if operador == multi:
    print(f"{operando} * {operando2} = {resultado_multi}")
if operador == division:
    print(f"{operando} / {operando2} = {resultado_divi}")
