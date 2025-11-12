from sort_words import order_list

def test_order_list_with_out_of_order_words():
    # Arrange
    list_input = ["python" , "variable" , "aaron" , "funcion" , "apple" , "computadora" , "monitor"]
    # Act
    result = order_list(list_input)
    # Assert
    assert result == sorted(list_input)


def test_order_list_with_empty_list():
    # Arrange
    list_input = []
    # Act
    result = order_list(list_input)
    # Assert
    assert result == sorted(list_input)