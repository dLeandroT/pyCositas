def run():


# Con Ciclo
    # cuadrados = []

    # for i in range(1, 11):
    #     if i % 3 == 0:
    #         continue    
    #     else:
    #         cuadrados.append(i**2)

    # print(cuadrados)

# Con Comprehension
    # cuadrados = [i**2 for i in range(0, 11) if i % 3 != 0]
    # print(cuadrados)


# Reto de la Clase
# List Comprehensions de los muktupolis de 4, de 9 y de 6 
# Que tengan maximo 5 cifras


    reto = [i for i in range(1, 100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]

    print(reto)

    # Tambien podria evaluar el modulo de 36. Es el mcm de los 3


if __name__ == '__main__':
    run()