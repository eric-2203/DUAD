def turn_string(word):
    reversed_word = ""
    for char in range(len(word) -1, -1, -1):
        reversed_word += word[char]
    print(reversed_word)

    return reversed_word


my_word = "Watermelon"

turn_string(my_word)