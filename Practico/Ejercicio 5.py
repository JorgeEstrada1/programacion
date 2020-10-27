def inversa(frase):
    cadena_inversa = ""
    for letra in frase:
        cadena_inversa = letra + cadena_inversa
    return cadena_inversa
frase = input("ingrese una frase: ")
inverso = inversa(frase)
print(inverso)