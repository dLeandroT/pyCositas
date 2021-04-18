def run():
    DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

    """
    Con los datos anteriores, Filtrar por:
    Trabajadores en Platzi
    Dominantes de Python
    Mayores de 25

    Tambien >  Crear un key adicional llamado old. Sera True si la 
        edad es mayor a 70, de contrario False.
    """

    ### Trabajadores en Platzi
    print("\n\n-- Trabajan en Platzi\n")
    platzi_workers = []

    # con LOOP
    platzi_workers.clear()
    for worker in DATA:
        name = worker["name"]
        if worker["organization"] == "Platzi":
            platzi_workers.append(name)
    print(f"Con LOOP\n  {platzi_workers}\n")

    # Con Comprehensions
    platzi_workers.clear()
    platzi_workers = [workers["name"] for workers in DATA 
        if workers["organization"] == "Platzi"]
    print(f"Con DictComprehensions\n   {platzi_workers}\n")

    # Con High Order Functions
    platzi_workers.clear()
    platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi" , DATA))
    platzi_workers = list(map (lambda worker: worker["name"], platzi_workers)) 
    print(f"Con HOF\n   {platzi_workers}")



    ### Dominantes de python
    print("\n\n-- Dominan Python\n")
    dominan_python = []

    # Con LOOP
    dominan_python.clear()
    for person in DATA:
        name = person["name"]
        if person["language"] == "python":
            dominan_python.append(name)
    print(f"Con LOOP\n  {dominan_python}\n")

    # Con Comprehensions
    dominan_python.clear()
    dominan_python = [person["name"] for person in DATA if person["language"] == "python"]
    print(f"Con DictComprehensions\n   {dominan_python}\n")

    # Con HOF
    dominan_python.clear()
    dominan_python = list(filter(lambda person: person["language"] == "python", DATA))
    dominan_python = list(map(lambda person: person["name"], dominan_python))
    print(f"Por HOF\n   {dominan_python}")



    ### Mayores de 25 
    print("\n\n-- Tienen mas de 25\n")
    personas_mayores_25 = []

    # Con LOOP
    personas_mayores_25.clear()
    for person in DATA:
        if person["age"] > 25:
            personas_mayores_25.append(person["name"])
    print(f"por LOOP\n   {personas_mayores_25}\n")

    # Con Compehensions
    personas_mayores_25.clear()
    personas_mayores_25 = [person["name"] for person in DATA if person["age"] > 25]
    print(f"con Comprehensions\n   {personas_mayores_25}\n")

    #Con High Order Functions
    personas_mayores_25.clear()
    personas_mayores_25 = list(filter(lambda person: person["age"] > 25, DATA))
    personas_mayores_25 = list(map(lambda person: person["name"], personas_mayores_25))
    print(f"con HOF\n   {personas_mayores_25}\n")




    """Compatible desed pyhton 3.9 en adelante"""
    ### old people
    print("\n\n-- Old People Tag")

    # con Comprehensions
    # old_people.clear()
    old_people = [person | {"old": person["age"] > 70} for person in DATA]
    print(old_people)

    # con HOF
    #   old_people = list(map(lambda person: person | {"old": person["age"] > 70}, DATA))
    


if __name__ == '__main__':
    run()