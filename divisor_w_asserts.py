def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0] 
    return divisors


def run():
        num = input("ingresa un numero entereo:   ")
        assert num.isnumeric(), "-- Debe ingresar un numero entero"
        num = int(num)
        assert num > 0, "-- Debe ingresar un numero positivo"
        print(divisors(num))
    
        
if __name__ == '__main__':
    run()

