import FreeSimpleGUI as sg
import logic as func
from datetime import datetime
import persistency as persist

manager = func.FinanceManager()

def add_category_window():
    layout = [
        [sg.Text("Nombre")], [sg.Input(key="nombre_categoria")],
        [sg.Text("Tipo")], [sg.Combo(["Ingreso", "Gasto"], key="tipo_categoria")],
        [sg.Button("Agregar"), sg.Button("Cerrar")]
    ]

    window = sg.Window("Add Category" , layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cerrar":
            break

        if event == "Agregar":
            name = values["nombre_categoria"]
            type = values["tipo_categoria"]

            if not name or not type:
                sg.popup_error("Todos los campos son obligatorios")

            else: 
                new_category = func.Category(name, type)
                manager.add_categories(new_category)
                sg.popup("Categoria agregada con exito!")
                window.close()
            

    window.close()


def add_movement_window():
    layout = [
        [sg.Text("Descripcion del movimiento")], [sg.Input(key="descripcion")],
        [sg.Text("Monto")], [sg.Input(key="monto")],
        [sg.Text("Fecha")], [sg.Input(key="fecha", default_text="DD-MM-YYYY")],
        [sg.Text("Categoria")], [sg.Combo([cat.name for cat in manager.categories], key="categoria")],
        [sg.Button("Agregar"), sg.Button("Cerrar")],
        
    ]

    window = sg.Window("Add Movement" , layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cerrar":
            break
        
        if event == "Agregar":
            amount = values["monto"]
            category_name  = values["categoria"]
            description = values["descripcion"]
            entered_date = values["fecha"]

            if not amount or not category_name or not description or not entered_date:
                sg.popup_error("Todos los campos son obligatorios.")

            else:
                try:
                    amount = float(amount)
                    if amount <= 0:
                        raise ValueError("El monto debe de ser un monto positivo.")
                    
                    category = None
                    for cat in manager.categories:
                        if cat.name == category_name:
                            category = cat
                            break
                    if not category:
                        sg.popup_error("Categoria invalida.")
                        continue
                    

                    datetime.strptime(entered_date, "%d-%m-%Y")

                    movement = func.Movement(category, amount, entered_date, description)
                    manager.add_movements(movement)
                    sg.popup("Movimiento agregado de manera exitosa.")
                    window.close()
                    #show_movements_window()
                except ValueError as error:
                    sg.popup_error(f"Hay algun error en los datos ingresados: {error}")

    window.close()


def show_movements_window():
    headers = ["Categoria", "Tipo", "Monto", "Fecha", "Descripcion"]
    data = manager.get_data_in_lists()
    layout = [
        [sg.Text("Todos los Movimientos")],
        [sg.Table(headings=headers, values=data, key="tabla_movimientos")],
        [sg.Button("Refrescar"), sg.Button("Cerrar")],
    ]

    window = sg.Window("Show movements", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cerrar":
            break
        elif event == "Refrrescar":
            window["tabla_movimientos"].update(values=manager.get_data_in_lists())

    window.close()

def main_layout():
    layout = [
        [sg.Text("Bienvenido al Gestor de Finanzas Personales")],
        [sg.Text(f"El balance en la cuenta es de: {manager.calculate_balance()}", key="account_balance")],
        [sg.Button("Agregar categoria"), sg.Button("Agregar Movimiento"), sg.Button("Mostrar movimientos")],
        [sg.Button("Cerrar Programa"), sg.Button("Exportar a CSV")]
    ]

    window = sg.Window("First program" , layout)
    
    manager.read_data()

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cerrar Programa":
            sg.popup("Gracias por utilizar nuestro Gestor de Finanzas!")
            break
        elif event == "Agregar categoria":
            add_category_window()
        elif event == "Agregar Movimiento":
            add_movement_window()
            window["account_balance"].update(f"El balance de la cuenta es de: {manager.calculate_balance()}")
        elif event == "Mostrar movimientos":
            show_movements_window()
        elif event == "Exportar a CSV":
            manager.export_data()
            sg.popup("Archivo exportado a CSV de manera exitosa.")

    window.close()


main_layout()