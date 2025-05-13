nombre = 'JUAN DANIEL'
apellido = 'muñoz queupul'
frase = 'hola como estas? es una frase'

longitud = len(frase)
print(longitud)
print(frase[len(frase) -1])

palabras = frase.split()
print(palabras)

mayusculas = apellido.upper()
print(mayusculas)

minusculas = nombre.lower()
print(minusculas)

mensaje = 'hola mundo'
print(mensaje)
cambio = mensaje.replace('hola', 'hola juna daniel tu puedes con el')
print(cambio)

for x in apellido:
    print(x)
