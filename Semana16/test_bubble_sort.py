import random
import pytest
from bubble_sort_1 import bubble_sort

def test_bubble_sort_with_small_list():
    # Arrange
    list_input = [5,4,3,2,1,6]
    # Act
    result = bubble_sort(list_input)
    # Assert
    assert result == [1, 2, 3, 4, 5, 6]


def test_bubble_sort_with_big_list():
    # Arrange
    list_input = [random.randint(1, 150) for x in range(150)]
    # Act
    result = bubble_sort(list_input)
    # Assert
    assert result == sorted(list_input)


def test_bubble_sort_with_empty_list():
    # Arrange
    list_input = []
    # Act
    result = bubble_sort(list_input)
    # Assert
    assert result == []

def test_bubble_sort_with_parameters_that_are_not_lists_or_numbers():
    # Arrange
    list_input = [3,2,"M"]
    # Act
    with pytest.raises(TypeError):
        bubble_sort(list_input)