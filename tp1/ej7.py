palabras = input("Ingresá varias palabras separadas por espacios: ").split()

oracion = []

for palabra in palabras: #palabra va tomando los valores de cada palabra de la lista palabras#
    if len(palabra) > 3: #len devuelve la cantidad de letras#
        oracion.append(palabra)

resultado = " ".join(oracion)

print("Oración final:", resultado)
