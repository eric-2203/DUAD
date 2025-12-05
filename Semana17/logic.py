# Crear toda la logica del programa para luego conectarla con la interfaz grafica.
import persistency as pers
import csv

class Category():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def show_info(self):
        return f"{self.name} ({self.type})"
    

class Movement():
    def __init__(self, category: Category, amount, date, description):
        self.category = category
        self.amount = int(amount)
        self.date = date
        self.description = description

    def show_details(self):
        return f"Categoria: {self.category.show_info()}, Monto: ₡{self.amount}, Fecha: {self.date}, Descripcion: {self.description}"
    
class FinanceManager():
    def __init__(self):
        self.movements = []
        self.categories = []

    def add_categories(self, new_category):
        self.categories.append(new_category)

    def has_categories(self):
        return len(self.categories) > 0
    
    def add_movements(self, new_movement):
        if not self.has_categories():
            raise ValueError("No hay ninguna categoria disponible.")
        self.movements.append(new_movement)
        return new_movement
    
    def show_all_movements(self):
        for mov in self.movements:
            print(mov.show_details())

    def get_data_in_lists(self):
        trans_details = []
        for mov in self.movements:
            data = [mov.category.name, mov.category.type, mov.amount, mov.date, mov.description]
            trans_details.append(data)

        return trans_details

    def calculate_balance(self):
        balance = 0
        for trans in self.movements:
            if trans.category.type == "Ingreso":
                balance = balance + trans.amount
            elif trans.category.type == "Gasto":
                balance = balance - trans.amount
        return f"₡{balance}"
    

    def export_data(self):
        pers.write_csv_file(self.get_data_in_lists())

    def read_data(self):
        self.movements = pers.read_file(Movement, Category)
        

    
#cat = Category("Comida", "Gasto")
#cat2 = Category("Salario", "Ingreso")
#cat3 = Category("Salud", "Gasto")


#mov3 = Movement(cat2, 100000, "05/11/2025", "Salario")
#mov = Movement(cat, 1250, "11/11/2025", "Pizza")
#mov2 = Movement(cat, 5000, "10/11/2025", "Ceviche")
#mov4 = Movement(cat3, 24000, "19/11/2025", "Gym")

manager = FinanceManager()

#manager.add_categories(cat)
#manager.add_categories(cat2)
#manager.add_categories(cat3)

#manager.add_movements(mov3)
#manager.add_movements(mov)
#manager.add_movements(mov2)
#manager.add_movements(mov4)

#manager.calculate_balance()

#manager.show_all_movements()
#print(manager.calculate_balance())