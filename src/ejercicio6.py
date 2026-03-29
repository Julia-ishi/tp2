# funciones ejercicio 6

def extraer_hashtags(post):
    palabras = post.split() # separo el post en palabras
    hashtags = []
    for palabra in palabras:
        if palabra.startswith("#"): # si la palabra empieza con # es un hashtag
            # saco signos como coma o punto si tiene
            hashtag = palabra.strip(".,")
            hashtags.append(hashtag)
    return hashtags # devuelve una lista con los hashtags encontrados en el post

def obtener_todos_los_hashtags(posts):
    todos = []
    for post in posts:
        hashtags = extraer_hashtags(post) # extraigo los hashtags de cada post
        todos.extend(hashtags) # agrego los hashtags a la lista de todos los hashtags
    return todos # devuelve una lista con todos los hashtags encontrados en todos los posts

def contar_frecuencias(hashtags):
    frecuencias = {}   # diccionario para contar la frecuencia de cada hashtag
    for hashtag in hashtags:
        if hashtag in frecuencias:
            frecuencias[hashtag] += 1
        else:
            frecuencias[hashtag] = 1
    return frecuencias

def obtener_trending(frecuencias):
    trending = {}
    for hashtag, cantidad in frecuencias.items(): #recorro el diccionario de frecuencias
        if cantidad > 1:
            trending[hashtag] = cantidad
    return trending     # devuelve un diccionario con los hashtags que tienen una frecuencia mayor a 1

def total_hashtags_unicos(frecuencias):
    return len(frecuencias)  # devuelve la cantidad de hashtags únicos