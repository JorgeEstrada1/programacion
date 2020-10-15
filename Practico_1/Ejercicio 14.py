estatura = float(input("ingrese su estatura: "))
peso = float(input("ingrese su peso: "))
edad = int(input("ingrese su edad: "))
masa = peso // (estatura **2)
if edad < 45 and masa <22.0:
    print("su riesgo es bajo")
elif edad < 45 and masa >= 22.0:
    print("su riesgo es medio")
elif edad >= 45 and masa < 22.0:
    print("su riesgo es medio")
elif edad >= 45 and masa >= 22.0:
    print("Su riesgo es alto")