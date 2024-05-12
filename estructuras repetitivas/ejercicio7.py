'''
La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad de Ibagué, 
cuantos entran con calcomanía de cada color. Conociendo el ultimo dígito de la placa de cada carro, 
se puede determinar el 
color de la calcomanía utilizando la siguiente relación:
'''

cantidadAmarilla = 0
cantidadRosa = 0
cantidadRoja = 0
cantidadVerde = 0
cantidadAzul = 0
totalAutos = int(input("Ingrese el número total de autos que entran a la ciudad: "))


for i in range(totalAutos):
    ultimo_digito = int(input(f"Ingrese el último dígito de la placa del auto {i+1}: "))
    
    if ultimo_digito == "amarilla":
        cantidadAmarilla += 1
    elif ultimo_digito == "rosa":
        cantidadRosa += 1
    elif ultimo_digito == "roja":
        cantidadRoja += 1
    elif ultimo_digito == "verde":
        cantidadVerde += 1
    elif ultimo_digito == "azul":
        cantidadAzul += 1
    else:
        print("ingrese un digito valido: ")


print("Cantidad de autos con calcomanía amarilla:", cantidadAmarilla)
print("Cantidad de autos con calcomanía rosa:", cantidadRosa)
print("Cantidad de autos con calcomanía roja:", cantidadRoja)
print("Cantidad de autos con calcomanía verde:", cantidadVerde)
print("Cantidad de autos con calcomanía azul:", cantidadAzul)






