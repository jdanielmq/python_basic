def calcular_calorias(carbohidratos, proteinas, grasas):
    calorias_carbo = carbohidratos * 4
    calorias_prote = proteinas * 4
    calorias_grasa = grasas * 9
    total_calorias = calorias_carbo + calorias_prote + calorias_grasa
    print(f'dentro de la funcion, la cantidad de calorias es las siguiente: {total_calorias}')

    return total_calorias


total = calcular_calorias(10,40,5)

print(f'Calorías totales: {total}')


