# funciones ejercicio 6
from collections import Counter

def extraer_hashtags(post):
    palabras = post.split()
    hashtags = []

    for palabra in palabras:
        if palabra.startswith("#"):
            hashtag = palabra.strip(".,")
            hashtags.append(hashtag)
    return hashtags

def obtener_todos_los_hashtags(posts):
    todos = []

    for post in posts:
        hashtags = extraer_hashtags(post)
        todos.extend(hashtags)
    return todos


def contar_frecuencias(posts):
    hashtags = obtener_todos_los_hashtags(posts)
    return Counter(hashtags)

def obtener_trending(frecuencias):
    trending = {}

    for hashtag, cantidad in frecuencias.items():
        if cantidad > 1:
            trending[hashtag] = cantidad
    return trending

def total_hashtags_unicos(frecuencias):
    return len(frecuencias)