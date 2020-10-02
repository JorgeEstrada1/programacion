partido_1 = "MAS"
partido2 = "UNIR"
print(partido_1, partido2)
partido = input("Indique por que partido politico quiere votar: ")
if partido == partido_1 or partido2:
    print(f"Usted a votado por {partido}")
else:
    print(f"Voto invalido {partido} no es ningun partido politico")