# funciones ejercicio 2
def convertir_a_segundos(duracion):
    minutos, segundos = duracion.split(":")
    return int(minutos) * 60 + int(segundos)

def calcular_duracion_total(playlist):
    total_segundos = 0

    for cancion in playlist:
        total_segundos += convertir_a_segundos(cancion["duration"])

    return total_segundos

def encontrar_cancion_mas_larga(playlist):
    mas_larga = None
    for cancion in playlist:
        total = convertir_a_segundos(cancion["duration"])

        if mas_larga is None or total > mas_larga[1]:
            mas_larga = (cancion["title"], total)
    return mas_larga

def encontrar_cancion_mas_corta(playlist):
    mas_corta = None
    for cancion in playlist:
        total = convertir_a_segundos(cancion["duration"])
        if mas_corta is None or total < mas_corta[1]:
            mas_corta = (cancion["title"], total)
    return mas_corta

def convertir_total_a_minutos_segundos(total_segundos):
    minutos = total_segundos // 60
    segundos = total_segundos % 60
    return minutos, segundos