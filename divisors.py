def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0] 
    return divisors

def run():
    num = int(input("ingresa un numero entereo:   "))
    print(divisors(num))
    



if __name__ == '__main__':
    run()