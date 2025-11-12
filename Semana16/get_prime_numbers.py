import random

def get_primes(list_of_numbers):
    primos = []
    for num in list_of_numbers:
        if num > 1:
            for numbers in range(2, num):
                if num % numbers == 0:
                    break
            else:
                primos.append(num)
    return primos

my_list = [1, 2, 15, 67, 18, 12, 17, 13, 19, 8, 10, 11]
primes = get_primes(my_list)
print(primes)