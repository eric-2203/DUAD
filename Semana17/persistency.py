# Agregar la logica para guardar y cargar archivos CSV
import csv
import os

def write_csv_file(movements_info):
    with open('movements_information.csv', mode='w', newline='', encoding='utf-8') as file:
        writer  = csv.writer(file)
        
        writer.writerow(["Categoria", "Tipo", "Monto", "Fecha", "Descripcion"])
        
        writer.writerows(movements_info)



def write_file(data):
    write_csv_file(data)


def read_file(movement_details, CategoryClass):
    object_movements = []
    try: 
        with open('movements_information.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                movement = movement_details(CategoryClass(row["Categoria"], row["Tipo"]), int(row["Monto"]), row["Fecha"], row["Descripcion"])
                object_movements.append(movement)
                
    except FileNotFoundError:
        return []

    return object_movements


def get_categories_from_file(CategoryClass):
    unique_categories = set()
    object_categories = []
    try: 
        with open('movements_information.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row["Categoria"]
                type = row["Tipo"]

                unique_categories.add((name, type))
        
        for name, type in unique_categories:
            object_categories.append(CategoryClass(name, type))

                
    except FileNotFoundError:
        return []

    return object_categories