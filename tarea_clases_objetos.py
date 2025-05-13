class ContadorPalabra:
    def __init__(self):
        self.contador = 0

    def contador(self, miarray):
        for x in miarray:
            if x != '':
                self.contador = self.contador + 1


    def  obtener_contador(self):
        return self.contador


frase = 'esta es una prueba de contador de palabras'   

evalucion = ContadorPalabra(0)
array = frase.split()
evalucion.contador(array)
obtener_contador = evalucion.obtener_contador()

print(f'la cantidad de palabras es la siguiente: ', obtener_contador)