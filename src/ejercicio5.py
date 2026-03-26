# funciones ejercicio 5

def zona_valida(zona):
    return zona in ["local", "regional", "nacional"]

def obtener_rango_peso(peso):
    if peso <= 1:
        return "hasta_1"
    elif peso <= 5:
        return "entre_1_y_5"
    else:
        return "mas_de_5"

def calcular_costo_envio(peso, zona):
    if not zona_valida(zona):
        return None
    rango = obtener_rango_peso(peso)
    if rango == "hasta_1":
        if zona == "local":
            return 500
        elif zona == "regional":
            return 1000
        else:
            return 2000
    elif rango == "entre_1_y_5":
        if zona == "local":
            return 1000
        elif zona == "regional":
            return 2500
        else:
            return 4500
    else:
        if zona == "local":
            return 2000
        elif zona == "regional":
            return 5000
        else:
            return 8000