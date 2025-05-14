class Animal:
    def __init__(self, nombre, sonido):
        self.nombre =  nombre
        self.sonido = sonido


    def mensaje(self):
        print(f'el animal es un {self.nombre} y su sonido es {self.sonido}')


class Tipo(Animal):
    def msg(self):
        return f'el animal ingresado es un {self.nombre} y el sonido que emiten {self.sonido}'
    

gato = Tipo('Gato', 'Miuau')
print(gato.msg())

perro = Tipo('Perro','Guau')
print(perro.msg())

