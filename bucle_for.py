frutas =  ['manzana', 'naranja', 'cereza']
contador = 0

for fruta in frutas:
    contador += 1
    print(f'fruta #{contador}: {fruta}')


numeros = [1, 2, 20, 4,5]
for numero in numeros:
    cuadrado = numero ** 2
    print(f'el cudarado del #{numero} es {cuadrado}')


notas = [1, 2, 3, 4, 5, 6, 7]
largo = len(numeros)
suma = 0;
promedio = 0.0
print('largo del array ', largo)
for nota in notas:
    suma += nota

promedio = suma / largo
print(f'suma es : {suma}')
print(f'el promedio es el siguiente:  {promedio}')
