"""
Crear un diccionario que tenga como llaves los numero del 1 al 1000 y como 
valores, sus raices cuadradas

Hacerlo Usando Dictionary Comprenhensions
"""

def run():
    # Prueba de funcionamiento
    # reto = {i: i**3 for i in range(1, 11) if i % 3 != 0}
    # print(reto) 

    numerosRaices = {i: round(i**0.5, 4) for i in range(1, 1000) }
    print(numerosRaices)


if __name__ == '__main__':
    run()