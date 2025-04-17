segundos = int(input("Introduce el número de segundos: "))
# Convierte los segundos a horas, minutos y segundos
# Imprime el resultado en formato de horas, minutos y segundos

minutos=segundos/60
horas=segundos/3600
print(int(horas),int(minutos%60),int(segundos%60))