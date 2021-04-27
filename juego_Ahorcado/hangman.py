import os
import random

def imprimir(archivo):
    """
    archivo = "ruta del archivo entre comillas"
     ej.:    imprimir("./directorio/archivo.txt") 
    """
    with open(archivo, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
        f.close()


def draw_bienvenida():
    os.system("clear")
    imprimir("./bienvenida.txt")
    input("\n\n\nPresiona ENTER para continuar...")
    print("_______________________________________")
        
    # Imprimir instrucciones
    os.system("clear")
    print("\n")
    imprimir("./instrucciones.txt")
    input("\n\nPresiona ENTER para continuar...")


def draw_progress(progress, score, progreso_ahorcado):
    os.system("clear")
    print("### A D I V I N A   L A   P A L A B R A ###")
    print("-------------------------------------------")
    print(f"puntaje:   {score}")
    print("-------------------------------------------")
    # Draw Ahorcado
    imprimir(f"./ahorcado/{progreso_ahorcado}.txt")
    print("\n\n\n", end="\t     ")
    for i in progress:
        print(i, end=" ")
    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def draw_final(secret_word, score, archivo):
    os.system("clear")
    print(f"puntaje final:  {score}")
    print("\n", end="\t\t")
    for letra in secret_word:
        print(letra, end=" ")
    print("")
    imprimir(archivo)


def quitar_acento(letra):
    remplazos = {'Á':'A', 'É':'E', 'Í':'I', 'Ó':'O', 'Ú':'U'}
    for key, value in remplazos.items():
        if letra == key:
            letra = value
    return (letra)


def choose_word():
    with open("./palabras.txt", "r", encoding="utf-8") as f:
        secret_words = [line.strip() for line in f]
        f.close()
    palabra = random.choice(secret_words)
    palabra  = palabra.upper()
    #  LIsta vacia para almacenar cada letra revisada
    palabra_revisada = []
    for letra in palabra:
        letra = quitar_acento(letra)
        palabra_revisada.append(letra)
    # Despues de revisa y quitar acentos, unir en un solo string 
    palabra = "".join(palabra_revisada)
    return palabra  

    
    

#  Funcion Principal
def run():
    draw_bienvenida()
    secret_word = choose_word()
    letras_ocultas = len(secret_word)
    hidden_word = ["_" for i in range(letras_ocultas)]


    # Para puntuacion
    score = 0
    limite_de_fallos = letras_ocultas * 2
    fallos = 0


    # Mapa de ahorcado
    posiciones_horca = [0, 0.14, 0.29, 0.44, 0.59, 0.8]
    progreso_ahorcado = 0
    
    
    # Gamelooop 
    is_gameover = False
    while not is_gameover:
        # CAlcuar POsicion de la Horca
        porcentaje = fallos/limite_de_fallos
        for i in posiciones_horca:
            if porcentaje > i:
              progreso_ahorcado = posiciones_horca.index(i)

        os.system("clear")
        draw_progress(hidden_word, score, progreso_ahorcado)
        letra_ingresada = input("Ingresa una letra:  ").upper()

        # Control de errores
        if len(letra_ingresada) == 0:
            os.system("clear")
            input("\n   ⚠ Recuerda ingresar una letra antes de dar ENTER...")
        elif len(letra_ingresada) > 1:
            os.system("clear")
            input("\n ⚠ Recuerda ingreasr solo UNA letra a la vez...")
        elif not letra_ingresada.isalpha():
            os.system("clear")
            input("\n ⚠ Recuerda que no hay numeros dentro de las palabras...")

        quitar_acento(letra_ingresada)
        
        # Comprobar la Letra
        control_puntos = letras_ocultas
        idx = 0
        for word in secret_word:
            if letra_ingresada == word:
                hidden_word[idx] = letra_ingresada
                letras_ocultas -= 1
                score += 100
            idx += 1
        if control_puntos == letras_ocultas:
            fallos += 1

        # Comprobar si hay victoria
        if letras_ocultas == 0:
            draw_final(secret_word, score, "./victoria.txt")
            is_gameover = True
        elif fallos == limite_de_fallos:
            draw_final(secret_word, score, "./derrota.txt")
            is_gameover = True



#Entry Point
if __name__ == '__main__':
    run()