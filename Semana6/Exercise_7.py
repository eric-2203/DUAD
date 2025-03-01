def get_prime_numbers (num=[]):
    for x in num:
        if x<=1:
            basura.append(x)
        #elif num == 2:
            #primos.append(num)
        for numbers in range(2,x):
            if x % numbers == 0:
                return False
        return primos.append(x)


primos= []
list= [2,3,4,5,6,7,8,9]
get_prime_numbers([1,2,3,4,5,6,7,8,9])
print(primos)