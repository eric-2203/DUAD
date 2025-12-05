# Agregar la logica para guardar y cargar archivos CSV
import csv
import os

def write_csv_file(movements_info):
    with open('movements_information.csv', mode='a', newline='', encoding='utf-8') as file:
        writer  = csv.writer(file)
        
        if os.path.getsize('movements_information.csv') == 0:
            writer.writerow(["Categoria", "Tipo", "Monto", "Fecha", "Descripcion"])
        
        writer.writerows(movements_info)


def check_if_file_is_empty(file):
    if file == 0:
        True
    elif file > 0:
        False


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