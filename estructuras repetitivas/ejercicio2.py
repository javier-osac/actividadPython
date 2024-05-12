'''
Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos números.
'''
suma_positivos = 0

for i in range(10):
    numero = float(input("Ingrese un número negativo: "))
    if numero < 0:
        numero = abs(numero)  
        suma_positivos += numero

print("La suma de los números positivos obtenidos de los negativos es:", suma_positivos)

