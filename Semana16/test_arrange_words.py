from arrange_words import turn_string

def test_turn_string_with_just_one_word():
    # Arrange
    word_input = "Pineapple"
    # Act
    result = turn_string(word_input)
    # Assert
    assert result == "elppaeniP"


def test_turn_string_with_phrases():
    # Arrange
    word_input = "Pineapple is a delicious fruit."
    # Act
    result = turn_string(word_input)
    # Assert
    assert result == ".tiurf suoiciled a si elppaeniP"


def test_turn_string_with_numbers_as_strings():
    # Arrange
    word_input = "123456789"
    # Act
    result = turn_string(word_input)
    # Assert
    assert result == "987654321"