def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firtName": "Deyvit", "lastName": "Tenjo"}


    # Super Lista de Diccionarios
    super_list = [
        {"firtName": "Deyvit", "lastName": "Tenjo"},
        {"firtName": "Leandro", "lastName": "Rocha"},
        {"firtName": "Jose", "lastName": "Jaramillo"},
        {"firtName": "Pedro", "lastName": "Smith"},
        {"firtName": "Miguel", "lastName": "Gomez"},
    ]

    # Super Diccionario de Listas
    super_dict = {
        "natural_num": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 4, 4, 5],
        "float_nums": [1.1, 2.7, 4.3, 6.1],
    }

    print("\n\nEste es el super dict")
    for key, value in super_dict.items():
        print (key, value)

    print("\n\nEste es la super list")
    for dic in super_list:
        for key, value in dic.items():
            print (key, value)



if __name__ == '__main__':
    run()