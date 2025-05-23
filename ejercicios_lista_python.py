def aumentar_biblioteca(nuevo_libro):
    archivo = open('libros.txt','r')
    libros = archivo.read().splitlines()
    archivo.close()
    
    libros += [nuevo_libro]
    return libros
    
def primer_libro_leido(libros):
    return libros[0]
    

nuevo_libro = 'Las Aventuras de Huckleberry Fin'

biblioteca = aumentar_biblioteca(nuevo_libro)

print('La biblioteca de libros leídos es:')
print(biblioteca)

primer_libro = primer_libro_leido(biblioteca)
print(f'El primer libro que he leído es: "{primer_libro}"')