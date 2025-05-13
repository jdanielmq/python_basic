# tarea de estudiante
noventa = 90.0
setenta = 70.0
sesenta = 60.0

nota = float(input('Ingrese la clasificación final : '))

if nota >= noventa:
    print('¡Felicidades! Has aprobado con una calificación sobresaliente.')
elif nota > setenta and nota < noventa:
    print('Has aprobado satisfactoriamente.')
elif nota > sesenta and nota < setenta:
    print('Has aprobado, pero necesitas mejorar un poco.')
elif nota < sesenta:
    print('Lo siento, has suspendido. Debes esforzarte más en la próxima evaluación.')

