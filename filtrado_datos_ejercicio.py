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
        edad es mayor a 50, de contrario False.
    """

    ### Trabajadores en Platzi
    print("\n\n-- Trabajan en Platzi\n")

    # con LOOP
    trabajadores = []
    for trabajador in DATA:
        name = trabajador["name"]
        if trabajador["organization"] == "Platzi":
            trabajadores.append(name)
    print(f"Con LOOP\n  {trabajadores}\n")

    # Con Comprehensions
    platzi_workers = [workers["name"] for workers in DATA 
        if workers["organization"] == "Platzi"]
    print(f"Con DictComprehensions\n   {platzi_workers}\n")

    # Con High Order Functions
    trabaja_platzi = list(filter(lambda trabaja: trabaja["organization"] == "Platzi" , DATA))
    trabaja_platzi = list(map (lambda trabaja: trabaja["name"], trabaja_platzi)) 
    print(f"Con HOF\n   {trabaja_platzi}")



    ### Dominantes de python
    print("\n\n-- Dominan Python\n")
    # Con LOOP
    python_pros = []
    for pro in DATA:
        name = pro["name"]
        if pro["language"] == "python":
            python_pros.append(name)
    print(f"Con LOOP\n  {python_pros}\n")

    # Con Comprehensions
    python_pro = [workers["name"] for workers in DATA if workers["language"] == "python"]
    print(f"Con DictComprehensions\n   {python_pro}\n")

    # Con HOF
    dominan_python = list(filter(lambda dompy: dompy["language"] == "python", DATA))
    dominan_python = list(map(lambda dompy: dompy["name"], dominan_python))
    print(f"Por HOF\n   {dominan_python}")




    ### Mayores de 25 
    print("\n\n-- Tienen mas de 25\n")
    # Con LOOP
    personas = []
    for persona in DATA:
        if int(persona["age"]) > 25:
            personas.append(persona["name"])
    print(f"por LOOP\n   {personas}\n")

    # Con Compehensions
    pMayores = [personas["name"] for personas in DATA if int(personas["age"]) > 25]
    print(f"con Comprehensions\n   {pMayores}\n")
    #Con High Order Functions
    personas_mayores = list(filter(lambda personas: int(personas["age"]) > 25, DATA))
    personas_mayores = list(map(lambda personas: personas["name"], personas_mayores))
    print(f"con HOF\n   {personas_mayores}\n")
    

if __name__ == '__main__':
    run()