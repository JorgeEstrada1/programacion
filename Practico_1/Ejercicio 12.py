num = int(input("Cantidad de palabras : "))
larga = ""
corta = ""
for i in range(1,num+1):
    palabra_in= input("palabra: ")
    if len(palabra_in) >= len(larga):
        larga = palabra_in
    elif len(palabra_in ) >= len(corta):
        corta = palabra_in
print(f"La palabra mas larga es {larga}")
print(f"La palabras mas corta es {corta}")
