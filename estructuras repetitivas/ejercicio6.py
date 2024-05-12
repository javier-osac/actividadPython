'''
Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un total de n personas.
'''
total= int(input("ingrese cuantos estudiantes hay: "))
hombres = 0 
mujeres = 0
for i in range (total): 
    genero = input(f"genero de la persona {i+1} (Hombre/Mujer): ").lower()

    if genero == "hombre":
        hombres +=1
    elif genero == "mujer":
        mujeres +=1
    else: 
        print ("ingrese hombre o mujer")
    
print("la cantidad de hombres que hay en el salon son : ",hombres)
print("la cantidad de mujeres que hay en el salon son: ",mujeres)
print("total de personas son: ",total)
       

        
