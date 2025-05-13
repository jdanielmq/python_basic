class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f'Hola, mi nombres {self.nombre} y tengo {self.edad} años.')


persona1 = Persona('Juan Daniel', 44)
persona1.saludar()

persona2 = Persona('Francisco Adrian', 29)
persona2.saludar()

