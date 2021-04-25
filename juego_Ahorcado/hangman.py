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


def quitar_acento(letra):
    remplazos = {'Á':'A', 'É':'E', 'Í':'I', 'Ó':'O', 'Ú':'U'}
    for key, value in remplazos.items():
        if letra == key:
            letra = value
    retun (letra)


def choose_word():
    with open("./palabras.txt", "r", encoding="utf-8") as f:
        secret_words = [line.strip() for line in f]
        f.close()
    palabra = random.choice(secret_words)
    palabra  = palabra.upper()
    for letra in palabra:
        quitar_acento(letra)
    print(palabra)    
    return palabra

    
    

#  Funcion Principal
def run():
    draw_bienvenida()
    secret_word = choose_word()
    # Gamelooop 
    is_gameover = False
    while not is_gameover:
        os.system("clear")
        # Pendiente imprimir el estado del colgado
        letra = input(" Ingresa una letra:  ")
        quitar_acento(letra)
        
       

        




#Entry Point
if __name__ == '__main__':
    run()