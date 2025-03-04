total_numbers = 10
lista_de_numeros = []
print("Ingrese 10 Números")
counter = 1
while (counter <= total_numbers):
    list_of_numbers= print("Ingrese Número" , counter)
    counter = counter + 1
    number = int(input())
    lista_de_numeros.append(number)
print("Los Números que usted ingresó son:" , lista_de_numeros)
for num in lista_de_numeros:
    numero_mayor = max(lista_de_numeros)
    #print(max(lista_de_numeros))
print("El número mayor es:" , max(lista_de_numeros))