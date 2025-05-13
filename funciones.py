def suma(num1, num2):
    result = num1+num2
    return result

def resta(num1, num2):
    result = num1 - num2
    return result

def division(num1, num2):
    result = num1 / num2
    return result

def multiplicacion(num1, num2):
    result = num1 * num2
    return result

num1 = int(input('ingrese un numero entero mayor a 0: '))
num2 = int(input('ingrese otro numero entero mayor a 0: '))
operacion = input('ingrese la operacion matematico [sumar(+), restar(-), multiplicar(*), dividir(/)]: ')
nombre = ''
if operacion == '+':
    nombre =  'suma'
    resultado = suma(num1,num2)
elif operacion == '-':
    nombre = 'resta'
    resultado = resta(num1,num2)
elif operacion == '/':
    nombre = 'división'
    resultado = division(num1,num2)
elif operacion == '*':
    nombre = 'multiplicación'
    resultado = multiplicacion(num1,num2)
    

if nombre != '':
    print(f'la {nombre} de los numeros es la siguiente: ', resultado)
else:
    print('La operación matematica no existe en la calculadora...!!!')








