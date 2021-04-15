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
    cuadrados = [i for i in range(0, 11) if i % 3 != 0]
    print(cuadrados)






if __name__ == '__main__':
    run()