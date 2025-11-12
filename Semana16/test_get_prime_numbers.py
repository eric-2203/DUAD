import random
from get_prime_numbers import get_primes

def test_get_prime_numbers_with_combined_numbers():
    # Arrange
    numbers_input = [1, 2, 15, 67, 18, 12, 13, 19, 8, 10, 11]
    # Act
    result = get_primes(numbers_input)
    # Assert
    assert result == [2, 67, 13, 19, 11]

def test_get_prime_numbers_with_just_number_1():
    # Arrange
    numbers_input = [1]
    # Act
    result = get_primes(numbers_input)
    # Assert
    assert result == []


def test_get_prime_numbers_without_prime_numbers():
    # Arrange
    numbers_input = [1, 15, 18, 12, 8, 10, 20, 22, 48, 6]
    # Act
    result = get_primes(numbers_input)
    # Assert
    assert result == []