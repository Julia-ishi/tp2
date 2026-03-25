# funciones ejercicio 3
def obtener_spoilers(entrada):
    spoilers = entrada.split(",")

    for i in range(len(spoilers)):
        spoilers[i] = spoilers[i].strip().lower()
    return spoilers

def limpiar_palabra(palabra):
    return palabra.strip(".,;:¡!¿?()").lower()

def reemplazar_spoilers(review, spoilers):
    palabras = review.split()
    resultado = []
    for palabra in palabras:
        palabra_limpia = limpiar_palabra(palabra)
        reemplazada = palabra

        for spoiler in spoilers:
            if palabra_limpia == spoiler:
                reemplazada = "*" * len(palabra_limpia)
        resultado.append(reemplazada)
    return " ".join(resultado)