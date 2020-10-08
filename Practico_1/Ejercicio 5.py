palabra = input("Ingresa una palabra: ")
palabra_2 = input("Ingresa otra palabra: ")
contar_palabra = len(palabra)
contar_palabra2 = len(palabra_2)
resultado = abs(contar_palabra - contar_palabra2)
if contar_palabra > contar_palabra2:
    print(f"La palabra {palabra} tiene {resultado} letras mas que {palabra_2} ")
if contar_palabra < contar_palabra2:
    print(f"La palabra {palabra_2} tiene {resultado} letras mas que {palabra}")
if contar_palabra == contar_palabra2:
    print("Las palabras tienen la misma cantidad de letras")
