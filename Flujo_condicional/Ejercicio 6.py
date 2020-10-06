año_bisiesto = int(input("Indique el año: "))
if año_bisiesto % 4 == 0:
    if año_bisiesto % 100 == 0:
        if año_bisiesto % 400 == 0:
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("EL año es bisiesto")
else:
    print("El año no es bisiesto")