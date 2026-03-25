#funciones ejercicio 1
def obtener_lineas(texto):
    return texto.splitlines()

def contar_lineas(lineas):
    return len(lineas)

def contar_palabras(lineas):
    total = 0
    for linea in lineas:
        palabras = linea.split()
        total += len(palabras)
    return total

def calcular_promedio(total_palabras, total_lineas):
    return total_palabras / total_lineas

def lineas_mayores_al_promedio(lineas, promedio):
    resultado = []
    for linea in lineas:
        cantidad = len(linea.split())
        if cantidad > promedio:
            resultado.append(linea)
    return resultado