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
    list_input = [27, 90, 3, 56, 75, 41, 85, 99, 11, 39, 93, 5, 59, 44, 25, 100, 63, 6, 96, 20, 84, 18, 4, 80, 30, 1, 91, 10, 43, 45, 21, 35, 26, 73, 33, 17, 64, 9, 74, 13, 71, 38, 15, 50, 95, 2, 22, 48, 24, 88, 12, 86, 52, 60, 62, 42, 36, 40, 98, 46, 31, 66, 34, 8, 14, 28, 32, 53, 55, 69, 76, 89, 7, 92, 19, 70, 16, 29, 37, 65, 61, 23, 94, 87, 47, 58, 49, 81, 77, 67, 78, 97, 72, 83, 68, 57, 82, 51, 79]
    # Act
    result = bubble_sort(list_input)
    # Assert
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


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