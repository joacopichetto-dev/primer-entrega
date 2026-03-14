import random

words = {
   "programacion":["python","variable","funcion","bucle"],
   "tipos_datos":["cadena","entero","lista"], 
   "informatica":["programa","codigo","archivo"]
}

print("¡Bienvenido al Ahorcado!")
print()

# mostrar categorias
for categoria in words:
    print("-", categoria)

# elegir categoria
categoria = input("elegir categoria: ")
while categoria not in words:
    print("Categoría no válida.")
    categoria = input("elegir categoria: ")

# palabras sin repetir
palabras = random.sample(words[categoria], len(words[categoria]))

for word in palabras:

    guessed = []
    attempts = 6
    score = 0

    print("\nNueva ronda")

    while attempts > 0:

        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "

        print(progress)

        # verificar si ganó
        if "_" not in progress:
            score += 6
            print("¡Ganaste!")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")

        # validacion
        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")

        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")

        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")

    else:
        score = 0
        print(f"¡Perdiste! La palabra era: {word}")

    print(f"Puntaje final: {score}")