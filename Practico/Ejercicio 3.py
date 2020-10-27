def longcadena(x):
    contador =0
    for i in (x):
        contador= contador +1
    return(contador)
def cadena(x):
    j= x.lower()
    return j[0].upper()+j[1:]
x =input("Ingrese una cadena: ")
print(cadena(x), "tiene", longcadena(x), "caracteres")