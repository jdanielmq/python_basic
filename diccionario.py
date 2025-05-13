personanew = {
    "nombre": "juan daniel",
    "edad" : 30,
    "ciudad" : "santiago de chile"
}

perfil = personanew

print(perfil)
print(perfil["nombre"])

personas = {
    "persona1":{
        "nombre": "juan daniel",
        "edad" : 30,
        "ciudad" : "santiago de chile"       
    },
    "persona2":{
        "nombre": "juan ",
        "edad" : 28,
        "ciudad" : " chile"       
    },  
    "persona3":{
        "nombre": " daniel",
        "edad" : 35,
        "ciudad" : "santiago"       
    }      
}

datos = personas["persona1"]
datos2 = personas["persona2"]
datos3 = personas["persona3"]

print(datos['nombre'])
print(datos2['nombre'])
print(datos3['nombre'])


persona1 = {
    "nombre" : None,
    "edad":None,
    "direccion":None,
    "telefono":None
}

datos_personales = persona1

datos_personales['nombre'] = input('Introduce un nombre: ')
datos_personales['edad'] = input('Introduce una edad: ')
datos_personales['direccion'] = input('Introduce una direccion: ')
datos_personales['telefono'] = input('Introduce  numero de telefono: ')

print(datos_personales)

print(datos_personales['nombre'], 'tiene', datos_personales["edad"],'años y vive en',datos_personales["direccion"], 'y su numero de telefono es', datos_personales['telefono'])
