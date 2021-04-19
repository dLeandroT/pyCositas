def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0] 
    return divisors

def run():
    try:
        num = int(input("ingresa un numero entereo:   "))
        if num < 0:
            raise ValueError("-- Debes ingresar un numero Positivo")
        print(divisors(num))
    except ValueError:
        print("---  Deber ingresar un numero")
        



if __name__ == '__main__':
    run()