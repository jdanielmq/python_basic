
contador = 0
palabras = (('manzana'), ('banana'), ('cereza'))
palabra_buscar = str(input('favor, ingrese un nombre de una fruta:'))
for nombre in palabras:
    if nombre == palabra_buscar:
        contador += 1 

if contador > 0:
    print('La palabra está en la tupla.')
else:
    print('La palabra NO está en la tupla.')