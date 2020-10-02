Monto_a_invertir = int(input("Ingrese cuanto quiere invertir: "))
interes_anual = int(input("Ingrese sus intereses anuales: "))
años_a_invertir = int(input("Ingrese cuantos años: "))
resultado = (1 + interes_anual) ** años_a_invertir
resultado = resultado * Monto_a_invertir
mensaje = f"Tu ganancia neta sera de {resultado}"
print(mensaje)