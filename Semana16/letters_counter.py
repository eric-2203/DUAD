def count_letters(my_string=""):
    upper_letters = 0
    lower_letters = 0
    for letters in my_string:
        if(letters.isupper()):
            upper_letters = upper_letters + 1
        elif(letters.islower()):
            lower_letters = lower_letters + 1

    print("Total Lower Case Letters:" ,lower_letters)
    print("Total Upper Case Letters:" ,upper_letters)

    return lower_letters, upper_letters


count_letters("Eric Flores Blanco")