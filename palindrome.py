def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("NO se pueden ingresar cadenas vacias")
        return string == string[::-1] 
    except ValueError as ve:
        print(ve)
        return False



def run():
    try:
        print (palindrome(""))
    except TypeError:
        print("Solo se puedem ingesar Strings")


if __name__ == '__main__':
    run()