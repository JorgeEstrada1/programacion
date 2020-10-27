def inversa(cadena):
    cadena_inversa = ""
    for caracter in cadena:
        cadena_inversa = caracter + cadena_inversa
    return cadena_inversa


def es_palindromo(original, inversa):
    for i in range(len(original) - 1):
        if (not (original[i] == inversa[i])):
            return False
    return True

cadena = input("Ingrese un texto: ")

cadena_inversa = inversa(cadena)

if (es_palindromo(cadena, cadena_inversa)):
    print("La cadena ingresada es un palindromo")
else:
    print("La cadena ingresada no es un palindromo")