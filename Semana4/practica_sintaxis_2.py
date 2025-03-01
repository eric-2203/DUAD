print("Ingrese su Nombre")
input()
print("Ingrese su Apellido")
input()
print("Ingrese su Edad")
edad = int(input())
if (edad <= 5): 
    print("Es bebé")
elif (edad <= 9):
    print("Es Niño")
elif (edad <= 12):
    print("Es Preadolescente")
elif (edad <= 19):
    print("Es Adolescente")
elif (edad <= 30):
    print("Es Adulto Joven")
elif (edad <= 59):
    print("Es Adulto")
elif (edad > 60):
    print("Es Adulto Mayor")

