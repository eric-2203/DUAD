from sum_numbers import add_numbers

def test_sum_numbers_with_small_numbers():
    # Arrange
    input_list = [5,5,6]
    # Act
    result = add_numbers(input_list)
    # Assert
    assert result == 16


def test_sum_numbers_with_big_numbers():
    # Arrange
    input_list = [5321, 1125, 6251]
    # Act
    result = add_numbers(input_list)
    # Assert
    assert result == 12697

def test_sum_numbers_with_negative_numbers():
    # Arrange
    input_list = [5,5,6, -5, -16]
    # Act
    result = add_numbers(input_list)
    # Assert
    assert result == -5