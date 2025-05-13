cero = 0
diez = 10
numero = int(input('favor, introduce un numero entero:'))

match numero:
    case numero if numero < cero:
        print('el numero ingresado es menor a 0')
    case numero if numero >= cero and numero < diez:
        print('el numero esta entre el ango de 0 al 10')
    case numero if numero >= diez:
        print('el numero es mayor que ', diez)
    case _:
        print('numero no reconocido')