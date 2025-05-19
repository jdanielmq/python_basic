# Palabra a adivinar
palabra_adivinar = "secreto"
 
def adivinar_palabra(letra_prueba, palabra_intento):
    """
    Determina si una letra está en una palabra específica y si un intento de palabra coincide con esa palabra.
 
    Args:
    letra_prueba (str): La letra a probar si está en la palabra.
    palabra_intento (str): La palabra intentada para adivinar la palabra correcta.
 
    Returns:
    None
    """
    # Verificar si la letra está en la palabra
    letra_en_palabra = letra_prueba in palabra_adivinar
    print(f"¿La letra de prueba se encuentra en la palabra? {letra_en_palabra}")
 
    # Verificar si la palabra de intento es igual a la palabra a adivinar y tiene la misma longitud
    resultado_adivinanza = palabra_intento == palabra_adivinar and len(palabra_intento) == len(palabra_adivinar)
    print(f"El jugador gana: {resultado_adivinanza}")
 
# Ejemplo de uso de la función
adivinar_palabra("s", "secreto")