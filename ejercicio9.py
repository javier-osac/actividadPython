'''
 Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos. 
'''
edadHombres = 0
edadMujeres = 0
sumaedadesTotal = 0
cantHombres = 0
cantMujeres = 0 


cantidaAlumnos = int(input("ingrese la cantidad de alumnos: "))

for i in range(cantidaAlumnos):
    genero = input(f"Ingrese el género del alumno {i+1} (M/F): ").lower()
    edad = int(input(f"Ingrese la edad del alumno {i+1}: "))
    if edad < 0:
        print("ingrese una edad valida")
        continue

    sumaedadesTotal += edad 
    if genero == "m":
        edadHombres += edad
        cantHombres +=edad 
    elif genero == "f":
        edadMujeres +=edad 
        cantMujeres +=edad
    else:
        print ("el genero ingresado no es correcto")


    promedioHombres = edadHombres /  cantHombres if cantHombres > 0 else 0 
    promedioMujeres = edadMujeres / cantMujeres if cantMujeres > 0 else 0 
    sumaedadesTotal = sumaedadesTotal / cantidaAlumnos if cantidaAlumnos > 0 else 0 

    print("Promedio de edades de hombres:", promedioHombres)
    print("Promedio de edades de mujeres:", promedioMujeres)
    print("Promedio de edades del grupo:", sumaedadesTotal)




  










