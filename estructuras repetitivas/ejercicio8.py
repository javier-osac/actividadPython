'''
un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un
algoritmo que lea por cada estudiante la calificación obtenida. Al finalizar calcule e
imprima:
• La cantidad de estudiantes que obtuvieron una calificación menor a 50.
• La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero
menor que 70.
• La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero
menor que 80.
• La cantidad de estudiantes que obtuvieron una calificación de 80 o más.
La calificación obtenida en el examen de algoritmia debe ser entre 1 y 100.
'''

calificacion_menor_50 = 0
calificacion_50_70 = 0
calificacion_70_80 = 0
calificacion_mas_80 = 0 
for i in range(5):
    calificacion = int(input("ingrese la calificacion del estudiante entre 1 a 100: "))
    if calificacion < 1 or calificacion > 100: 
        print("la calificaion debe ser de 1 a 100, intente de nuevo")
        continue


    if calificacion < 50:
        calificacion_menor_50 +=1
    elif calificacion < 70:
        calificacion_50_70 +=1
    
    elif calificacion <80:
        calificacion_70_80 +=1
    else:
        calificacion_mas_80 +=1

    

print ("La cantidad de estudiantes que obtuvieron una calificación menor a 50: ",calificacion_menor_50)
print ("La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70: ",calificacion_50_70)
print ("La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80: ",calificacion_70_80)
print("La cantidad de estudiantes que obtuvieron una calificación de 80 o más: ",calificacion_mas_80)





    

