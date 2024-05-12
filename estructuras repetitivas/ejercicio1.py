'''
Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros.
'''
contador = 0
numerosPostivos = 0
numerosNegativos = 0
numerosNeutros = 0
for i in range (1,20):
    digitos = float(input("Ingrese los valores: "))
 

    if digitos > 0:
        numerosPostivos  += 1
    elif digitos < 0:
        numerosNegativos +=1 
    else:
        numerosNeutros +=1 
     

    print("los numeros postivos son: ", numerosPostivos)
    print("los numero negativos son: ", numerosNegativos)
    print("los numeros neutros son: ",numerosNeutros)
            