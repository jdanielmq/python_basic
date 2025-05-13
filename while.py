suma = 0
contador = 1

numero = int(input('ingrese un numero positivo (o un numero negativo para salir):'))

while contador <= numero:
    print('numero actual:', contador)
    suma += contador
    contador += 1

print('La suma del conteo es:', suma)
print('conteo terminado...!!!')