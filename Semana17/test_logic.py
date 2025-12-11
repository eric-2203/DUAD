from logic import FinanceManager
from logic import Category
from logic import Movement
import pytest


def test_calculate_balance():
    #Arrange
    manager = FinanceManager()
    category_a = Category("Salario", "Ingreso")
    category_b = Category("Comida", "Gasto")
    movement_1 = Movement(category_a, 250000, "15-11-2025", "Quincena Nov")
    movement_2 = Movement(category_b, 11000, "25-11-2025", "Pizza")
    manager.add_categories(category_a)
    manager.add_categories(category_b)
    manager.add_movements(movement_1)
    manager.add_movements(movement_2)
    #Act
    result = manager.calculate_balance()
    #Assert
    assert result == 239000


def test_if_movements_get_added_to_the_list():
    #Arrange
    manager = FinanceManager()
    category_a = Category("Salario", "Ingreso")
    movement_1 = Movement(category_a, 250000, "15-11-2025", "Quincena Nov")
    manager.add_categories(category_a)
    #Act
    result = manager.add_movements(movement_1)
    #Assert
    assert result == manager.movements[0] == movement_1

def test_if_movements_get_added_to_the_list_without_category():
    #Arrange
    manager = FinanceManager()
    category_a = Category("Salario", "Ingreso")
    movement_1 = Movement(category_a, 250000, "15-11-2025", "Quincena Nov")
    #Act
    
    with pytest.raises(ValueError):
        manager.add_movements(movement_1)



def test_if_categories_get_added_to_the_list():
    #Arrange
    manager = FinanceManager()
    category_a = Category("Salario", "Ingreso")
    movement_1 = Movement(category_a, 250000, "15-11-2025", "Quincena Nov")
    #Act
    result = manager.add_categories(category_a)
    #Assert
    assert result == manager.categories[0] == category_a


