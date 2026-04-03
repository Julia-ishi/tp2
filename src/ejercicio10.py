def crear_estadisticas(participantes):
    #Crea las estadisticas iniciales de cada participante
    estadisticas = {} 
    for participante in participantes:
        estadisticas[participante] = {
            "puntaje_total": 0,
            "rondas_ganadas": 0,
            "mejor_ronda": 0,
            "puntajes": []
        }
    return estadisticas

def calcular_puntaje(puntajes_jueces):
    #Suma los puntajes de los tres jueces
    total = 0
    for juez in puntajes_jueces:
        total += puntajes_jueces[juez] #Suma el puntaje del juez al total
    return total

def obtener_participantes(rounds):
    #Obtiene los participantes de la primera ronda
    return list(rounds[0]["scores"].keys()) #Obtiene los nombres de los participantes de la primera ronda y los devuelve como una lista

def procesar_ronda(ronda,estadisticas):
    #Procesa una ronda y actualiza las estadisticas
    puntajes_ronda = {}
    for participante in ronda["scores"]:
        puntaje = calcular_puntaje(ronda["scores"][participante])
        puntajes_ronda[participante] = puntaje
        estadisticas[participante]["puntaje_total"] += puntaje
        estadisticas[participante]["puntajes"].append(puntaje)
        if puntaje > estadisticas[participante]["mejor_ronda"]:
            estadisticas[participante]["mejor_ronda"] = puntaje
    ganador = max(puntajes_ronda, key=puntajes_ronda.get) #Obtiene el participante con el puntaje mas alto en la ronda
    estadisticas[ganador]["rondas_ganadas"] += 1
    return ganador,puntajes_ronda

def calcular_promedio(lista):
    #Calcula el promedio de la lista
    if len(lista) == 0:
        promedio = 0
    else:
        promedio = sum(lista) / len(lista)
    return promedio

def armar_tabla(estadisticas):
    #Arma la tabla de posiciones
    tabla = []
    for participante in estadisticas:
        datos = estadisticas[participante] #Obtiene los datos del participante
        fila = {
            "nombre": participante,
            "puntaje_total": datos["puntaje_total"],
            "rondas_ganadas": datos["rondas_ganadas"],
            "mejor_ronda": datos["mejor_ronda"],
            "promedio": calcular_promedio(datos["puntajes"])
        }
        tabla.append(fila)
    tabla = sorted(tabla, key=lambda elemento: elemento["puntaje_total"], reverse=True) #Ordena la tabla por puntaje total de mayor a menor
    return tabla

def imprimir_tabla(tabla,titulo):
    #Imprime la tabla de posiciones con un titulo
    print(titulo)
    print()
    for fila in tabla:
        print("Cocinero:",fila["nombre"])
        print("  Puntaje total:",fila["puntaje_total"])
        print("  Rondas ganadas:",fila["rondas_ganadas"])
        print("  Mejor ronda:",fila["mejor_ronda"])
        print("  Promedio:", round(fila["promedio"], 1))
        print("-" * 30)
    print()

def mostrar_resultados_competencia(rounds):
    #muestra los resultados de la competencia procesando cada ronda y actualizando las estadisticas
    participantes = obtener_participantes(rounds)
    estadisticas = crear_estadisticas(participantes)
    numero_ronda = 1
    for ronda in rounds:
        ganador,puntajes_ronda = procesar_ronda(ronda,estadisticas)
        print(f"Ronda {numero_ronda} - {ronda['theme']}:") 
        print(f"Ganador: {ganador} ({puntajes_ronda[ganador]} pts)")
        print()
        tabla = armar_tabla(estadisticas)
        imprimir_tabla(tabla,"Tabla de posiciones:")
        numero_ronda += 1
    tabla_final = armar_tabla(estadisticas)
    imprimir_tabla(tabla_final, "Tabla de posiciones final:")