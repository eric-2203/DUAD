def get_primes(lista):
    primos = []
    for num in lista:
        if num > 1:
            for numbers in range(2, num):
                if num % numbers == 0:
                    break
            else:
                primos.append(num)
    return primos

mi_lista = [1, 4, 6, 7, 13, 9, 67]
primes = get_primes(mi_lista)
print(primes)