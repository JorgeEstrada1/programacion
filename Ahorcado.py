def imprimirAhorcado(intentos):
    if(intentos==5):
        print("================")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("===")
    if (intentos == 4):
        print("================")
        print("=              |")
        print("=              ()")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("===")
    if (intentos == 3):
        print("================")
        print("=              |")
        print("=              ()")
        print("=            ------")
        print("=")
        print("=")
        print("=")
        print("=")
        print("===")
    if (intentos == 2):
        print("================")
        print("=              |")
        print("=              ()")
        print("=           /------\ ")
        print("=)              |    ")
        print("=                    " )
        print("=")
        print("=")
        print("===")
    if (intentos == 1):
        print("================")
        print("=              |")
        print("=              ()")
        print("=           /------ \ ")
        print("=          /    |    \ ")
        print("=               |       " )
        print("=               |       " )
        print("=                       " )
        print("===                     " )
    if (intentos == 0):
        print("================")
        print("=              |")
        print("=              ()")
        print("=           /------ \ ")
        print("=          /    |    \ ")
        print("=               |       " )
        print("=               |       " )
        print("=               |       " )
        print("===            / \      " )


archivoPalabras=open("palabras_sencillas.txt","r")

listaPalabrasOcultas=archivoPalabras.readlines()

#palabraoculta=listaPalabrasOcultas[2]
archivoPalabras.close()


for palabraoculta in listaPalabrasOcultas:


    #palabraoculta=palabraoculta.replace("\n","")
    palabraoculta = palabraoculta.strip()

    tam=len(palabraoculta)
    vectorPalabraOculta=[]
    vectorPalabraGuiones=[]
    intentos=6

    for pos in range (0,tam,1):
        vectorPalabraOculta.append(str(palabraoculta[pos]))
        vectorPalabraGuiones.append("-")


    print(vectorPalabraGuiones)
    while(intentos>0):

        print("Cantidad de intentos: ",intentos)
        coincidencias=0
        cantidadguiones=0
        letra=input("Ingrese una letra: ")
        letra=letra.upper()
        for pos in range(0,tam,1):
            if(letra==vectorPalabraOculta[pos]):
                vectorPalabraGuiones[pos]=letra
                coincidencias=coincidencias+1


        print(vectorPalabraGuiones)

        for pos in range(0,tam,1):
            if(vectorPalabraGuiones[pos]=="-"):
                cantidadguiones=cantidadguiones+1

        if(coincidencias==0):
            intentos=intentos-1
            imprimirAhorcado(intentos)

        if(cantidadguiones==0):
            print("Ganaste, adivinaste la palabra")
            intentos=-1


    if(intentos==0):
        print("Se terminaron tus intentos!")

archivoPalabras=open("palabras_intermedias.txt","r")

listaPalabrasOcultas=archivoPalabras.readlines()

#palabraoculta=listaPalabrasOcultas[2]
archivoPalabras.close()


for palabraoculta in listaPalabrasOcultas:


    #palabraoculta=palabraoculta.replace("\n","")
    palabraoculta = palabraoculta.strip()

    tam=len(palabraoculta)
    vectorPalabraOculta=[]
    vectorPalabraGuiones=[]
    intentos=6

    for pos in range (0,tam,1):
        vectorPalabraOculta.append(str(palabraoculta[pos]))
        vectorPalabraGuiones.append("-")


    print(vectorPalabraGuiones)
    while(intentos>0):

        print("Cantidad de intentos: ",intentos)
        coincidencias=0
        cantidadguiones=0
        letra=input("Ingrese una letra: ")
        letra=letra.upper()
        for pos in range(0,tam,1):
            if(letra==vectorPalabraOculta[pos]):
                vectorPalabraGuiones[pos]=letra
                coincidencias=coincidencias+1


        print(vectorPalabraGuiones)

        for pos in range(0,tam,1):
            if(vectorPalabraGuiones[pos]=="-"):
                cantidadguiones=cantidadguiones+1

        if(coincidencias==0):
            intentos=intentos-1
            imprimirAhorcado(intentos)

        if(cantidadguiones==0):
            print("Ganaste, adivinaste la palabra")
            intentos=-1


    if(intentos==0):
        print("Se terminaron tus intentos!")


archivoPalabras=open("palabras_complejas.txt","r")

listaPalabrasOcultas=archivoPalabras.readlines()

#palabraoculta=listaPalabrasOcultas[2]
archivoPalabras.close()


for palabraoculta in listaPalabrasOcultas:


    #palabraoculta=palabraoculta.replace("\n","")
    palabraoculta = palabraoculta.strip()

    tam=len(palabraoculta)
    vectorPalabraOculta=[]
    vectorPalabraGuiones=[]
    intentos=6

    for pos in range (0,tam,1):
        vectorPalabraOculta.append(str(palabraoculta[pos]))
        vectorPalabraGuiones.append("-")


    print(vectorPalabraGuiones)
    while(intentos>0):

        print("Cantidad de intentos: ",intentos)
        coincidencias=0
        cantidadguiones=0
        letra=input("Ingrese una letra: ")
        letra=letra.upper()
        for pos in range(0,tam,1):
            if(letra==vectorPalabraOculta[pos]):
                vectorPalabraGuiones[pos]=letra
                coincidencias=coincidencias+1


        print(vectorPalabraGuiones)

        for pos in range(0,tam,1):
            if(vectorPalabraGuiones[pos]=="-"):
                cantidadguiones=cantidadguiones+1

        if(coincidencias==0):
            intentos=intentos-1
            imprimirAhorcado(intentos)

        if(cantidadguiones==0):
            print("Ganaste, adivinaste la palabra")
            intentos=-1


    if(intentos==0):
        print("Se terminaron tus intentos!")


