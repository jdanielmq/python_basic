personas = (('juan',25), ('jose', 16), ('pancho', 29))

for nombre, edad in personas:
    if edad > 20:
        print(f'nombre es {nombre} y la edad {edad}')


numeros = (10,20,30,40,50,60,70,80,90,100,1000,5000,10000)
suma = sum(numeros)

print(f'la suma de los numeros es {suma}')


frutas = (('manzana'), ('banana'), ('cereza'))
palabra_buscar = str(input('favor, ingrese un nombre de una fruta:'))
for nombre in frutas:
    if nombre == palabra_buscar:
        print('La palabra está en la tupla.')

print('La palabra NO está en la tupla.')