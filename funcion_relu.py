from math import e

def relu(x):
    """ calcula el resultado de la funcion matematicas Relu."""
    return max(0,x)



def sigmoid(x):
    """Se va a calcular la funcion de matematica sigmoid """
    return 1 / (1 + e**(-x))


def sinh(x):
    return (e**x - e**(-x)) / 2

def cosh(x):
    return (e**x + e**(-x))/2  

def tanh(x):
    return (sinh(x) / cosh(x)) 


valor  =  relu(0)
print(valor)
print(e)
valor_dos = sigmoid(-10)
print(valor_dos)


resultado = tanh(0)
print(resultado)