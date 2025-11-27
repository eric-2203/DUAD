# Agregar la logica para guardar y cargar archivos CSV
import csv
import logic as func

my_manager = func.FinanceManager()

def write_csv_file(movements_data, data):
    with open('movements_information.csv', mode='a', newline='', encoding='utf-8') as file:
        writer  = csv.writer(file)

        writer.writerow(["Categoria", "Monto", "Fecha", "Descripcion"])

        writer.writerows(data)


def write_file():
    movements_data = my_manager.get_data_in_lists()
    write_csv_file('students_information.csv', movements_data)