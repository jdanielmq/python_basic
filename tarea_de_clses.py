class Animal:
    def __init__(self, nombre):
        self.nombre =  nombre
        self.sonido = ''
        return

    def mensaje(self):
        print(f'el animal es un {self.nombre}')
        return


class Tipo(Animal):
    def idioma(self, sonido):
        self.sonido = sonido
        return
    
    def hablar(self):
        return f'el animal ingresado es un {self.nombre} y el sonido que emiten es {self.sonido}'
    

gato = Tipo('Gato')
gato.idioma('Miau')
print(gato.hablar())
print(gato.mensaje())

perro = Tipo('Perro')
perro.idioma('Guau')
print(perro.hablar())
print(perro.mensaje())
