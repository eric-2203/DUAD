list_a = ["first_name" , "last_name" , "role"]
list_b = ["Eric" , "Flores" , "Customer Service Associate"]
dictionary = {}
for keys in range(len(list_a)):
    keys=list_a[keys]
    values=list_b[keys]
    dictionary[keys]=values
print(dictionary)