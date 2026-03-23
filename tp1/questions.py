import random

categorias = {
    "programacion": [
        "python",
        "programa",
        "variable",
        "funcion",
        "bucle"
    ],
    "tipos de datos": [
        "cadena",
        "entero",
        "lista"
    ]
}

print("¡Bienvenido al Ahorcado!")
print()
print("Categorías disponibles:")

for categoria in categorias:
    print("-", categoria)

print()
opcion = input("Elegí una categoría: ")

while opcion not in categorias:
    print("Categoría no válida")
    opcion = input("Elegí una categoría: ")

palabras = random.sample(categorias[opcion], len(categorias[opcion]))

for word in palabras:
    guessed = []
    attempts = 6
    puntaje = 0

    print()
    print("Nueva ronda")

    while attempts > 0:
        progress = ""

        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "

        print(progress)

        if "_" not in progress:
            print("¡Ganaste!")
            puntaje += 6
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida")
        elif letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1
            print("Esa letra no está en la palabra.")

        print()

    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje = 0

    print(f"Puntaje final: {puntaje}")