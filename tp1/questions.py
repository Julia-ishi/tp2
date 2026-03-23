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
for categoria in categorias:
    print("-", categoria)

print()
opcion = input("Elegí una categoría: ")

while opcion not in categorias:
    print("Categoría no válida")
    opcion = input("Elegí una categoría: ")

palabras = random.sample(categorias[opcion], len(categorias[opcion])) #genero una lista de palabras aleatorias de la categoría elegida, sin repetir ninguna
for word in palabras:
  guessed = []
  attempts = 6
  print()
  while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    
    letter = input("Ingresá una letra: ")
    if len(letter) != 1 or not letter.isalpha(): #me fijo que solo sea un caracter y que sea una letra
        print("Entrada no válida")
        print()
    else:

      if letter in guessed:
        print("Ya usaste esa letra.")
      elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
      else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")
    print()
  else:
    print(f"¡Perdiste! La palabra era: {word}")
  print(f"puntaje final: {attempts}")