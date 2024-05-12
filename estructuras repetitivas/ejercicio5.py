'''
Una persona debe realizar un muestreo con 50 personas para determinar el promedio de 
peso de los niños, jóvenes, adultos y ancianos que existen en su zona.
'''

import random


peso_ninos = (10, 40)
peso_jovenes = (50, 70)
peso_adultos = (60, 90)
peso_ancianos = (50, 80)


datos_peso = []
for _ in range(50):
   
    edad = random.randint(1, 100)
    
    # Asignar un peso según la edad
    if edad <= 12:  # Niños
        peso = random.uniform(peso_ninos[0], peso_ninos[1])
    elif 13 <= edad <= 30:  # Jóvenes
        peso = random.uniform(peso_jovenes[0], peso_jovenes[1])
    elif 31 <= edad <= 60:  # Adultos
        peso = random.uniform(peso_adultos[0], peso_adultos[1])
    else:  # Ancianos
        peso = random.uniform(peso_ancianos[0], peso_ancianos[1])
    
    datos_peso.append(peso)

#
promedio_ninos = sum(peso for peso in datos_peso if peso <= peso_ninos[1]) / 50
promedio_jovenes = sum(peso for peso in datos_peso if peso <= peso_jovenes[1] and peso > peso_ninos[1]) / 50
promedio_adultos = sum(peso for peso in datos_peso if peso <= peso_adultos[1] and peso > peso_jovenes[1]) / 50
promedio_ancianos = sum(peso for peso in datos_peso if peso <= peso_ancianos[1] and peso > peso_adultos[1]) / 50


print("Promedio de peso de niños:", promedio_ninos)
print("Promedio de peso de jóvenes:", promedio_jovenes)
print("Promedio de peso de adultos:", promedio_adultos)
print("Promedio de peso de ancianos:", promedio_ancianos)

