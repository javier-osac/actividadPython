'''
Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos. 
Realizar un algoritmo para calcular el promedio y la 
calificación más alta y más baja de todo el grupo.
'''

calificaciones = []


for i in range(20):
    calificacion = float(input(f"Ingrese la calificación del alumno {i + 1}: "))
    calificaciones.append(calificacion)


promedio = sum(calificaciones) / len(calificaciones)


calificacion_maxima = max(calificaciones)
calificacion_minima = min(calificaciones)


print("Promedio de calificaciones:", promedio)
print("Calificación más alta:", calificacion_maxima)
print("Calificación más baja:", calificacion_minima)

