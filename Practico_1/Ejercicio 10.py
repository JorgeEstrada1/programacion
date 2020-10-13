tiempo_total = 0
duracion = int(input("Duracion tramo: "))
while (duracion != 0):
	tiempo_total=tiempo_total + duracion
	duracion = int(input("Duracion tramo: "))
print ("Tiempo total del viaje:",str(tiempo_total/60)+":"+str(tiempo_total%60),"horas")