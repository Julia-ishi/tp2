# funciones ejercicio 4

def tiene_un_solo_arroba(email):
    return email.count("@") == 1


def tiene_texto_antes_arroba(email):
    partes = email.split("@")
    return len(partes[0]) > 0


def tiene_punto_despues_arroba(email):
    partes = email.split("@")
    if len(partes) < 2:
        return False
    return "." in partes[1]


def no_empieza_ni_termina_mal(email):
    return not (email.startswith("@") or email.endswith("@") or email.startswith(".") or email.endswith("."))


def dominio_valido(email):
    partes = email.split(".")
    if len(partes) < 2:
        return False
    return len(partes[-1]) >= 2


def validar_email(email):
    return (
        tiene_un_solo_arroba(email)
        and tiene_texto_antes_arroba(email)
        and tiene_punto_despues_arroba(email)
        and no_empieza_ni_termina_mal(email)
        and dominio_valido(email)
    )