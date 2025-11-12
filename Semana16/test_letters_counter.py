from letters_counter import count_letters

def test_count_letters_with_mixed_letters():
    # Arrange
    text_input = "Eric Flores Blanco"
    # Act
    result = count_letters(text_input)
    # Assert
    assert result == (13, 3)


def test_count_letters_only_with_lower_case_letters():
    # Arrange
    text_input = "eric flores blanco"
    # Act
    result = count_letters(text_input)
    # Assert
    assert result == (16, 0)

def test_count_letters_with_symbols_numbers_and_letters():
    # Arrange
    text_input = "Eric!, Flores? blanco. &%$"
    # Act
    result = count_letters(text_input)
    # Assert
    assert result == (14, 2)