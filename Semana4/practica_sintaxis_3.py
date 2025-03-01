import random
print("Ingrese un Número")
numero = int(input())
secret_numbers = random.randint(1, 10)
while (numero != secret_numbers):
    print("Intente de Nuevo")
    numero = int(input())
else: print("Lo Lograste")
