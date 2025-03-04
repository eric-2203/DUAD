cantidad_total_de_notas=0
notas_reprobadas=0
notas_aprobadas=0
promedio_notas_reprobadas=0
promedio_notas_aprobadas=0
promedio_total_de_notas=0
print("Ingrese la cantidad total de notas")
cantidad_total_de_notas = int(input())
contador_de_nota = 1
while (contador_de_nota <= cantidad_total_de_notas): 
    print("Ingrese Nota Número:" , contador_de_nota)
    contador_de_nota = contador_de_nota + 1
    nota = int(input())
    if nota < int(70):
        notas_reprobadas = notas_reprobadas + 1
        promedio_notas_reprobadas = promedio_notas_reprobadas + nota
    else:
        notas_aprobadas = notas_aprobadas + 1
        promedio_notas_aprobadas = promedio_notas_aprobadas + nota
    promedio_total_de_notas = promedio_total_de_notas + (nota / cantidad_total_de_notas)
promedio_notas_reprobadas = promedio_notas_reprobadas / notas_reprobadas
promedio_notas_aprobadas = promedio_notas_aprobadas / notas_aprobadas
print("La cantidad de notas reprobadas es de:" , notas_reprobadas)
print("La cantidad de notas aprobadas es de:" , notas_aprobadas)
print("El promedio de notas reprobadas es de:" , promedio_notas_reprobadas)
print("El promedio de notas aprobadas es de:" , promedio_notas_aprobadas)
print("El promedio total de notas es de:" , promedio_total_de_notas)
if promedio_total_de_notas >= 70: 
    print("Aprobaste")
else:
    print("Reprobaste")