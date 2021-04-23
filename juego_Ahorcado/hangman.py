import os

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
        
    # Imprimir instrucciones
    print("\n\n")
    imprimir("./instrucciones.txt")
    input("\n\nPresiona ENTER para continuar...")



    


def run():
    draw_bienvenida()





#Entry Point
if __name__ == '__main__':
    run()