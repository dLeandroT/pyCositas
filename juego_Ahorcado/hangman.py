import os
import random

def imprimir(archivo):
    """
    archivo = "ruta del archivo entre comillas"
     ej.:    imprimir("./directorio/archivo.txt") 
    """
    with open(archivo, "r", encoding="utf-8") as f:
        for line in f:
            print(line)
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


def draw_progress(progress):
    os.system("clear")
    print("### A D I V I N A   L A   P A L A B R A ###\n\n\n", end="\t\t")
    for i in progress:
        print(i, end=" ")
    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


def draw_victoria(secret_word):
    os.system("clear")
    print("\n", end="\t\t")
    for letra in secret_word:
        print(letra, end=" ")
    print("")
    imprimir("./victoria.txt")
    


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
    

    # Gamelooop 
    is_gameover = False
    while not is_gameover:
        os.system("clear")
        draw_progress(hidden_word)
        letra_ingresada = input("Ingresa una letra:  ").upper()
        quitar_acento(letra_ingresada)
        
        # Comprobar la Letra
        idx = 0
        for word in secret_word:
            if letra_ingresada == word:
                hidden_word[idx] = letra_ingresada
                letras_ocultas -= 1
            idx += 1

        # Comprobar si hay victoria
        if letras_ocultas == 0:
            is_gameover = True
        
    draw_victoria(secret_word)
       




#Entry Point
if __name__ == '__main__':
    run()