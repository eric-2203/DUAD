def get_numbers():
    while True:
        try:
            number = int(input("Write a number: "))
            return number
        except ValueError:
            print("The value needs to be a number")



def get_operations():
    print("""
    Options:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Clear Result
    6. Exit
    """)
    while True:
        try: 
            operation = int(input("Choose an option from the menu: "))
            if operation in [1, 2, 3, 4, 5, 6]:
                return operation
            else:
                print("Invalid operation. Choose an option from the menu")
        except  ValueError:
            print("The value you used is not valid. Select an option from the menu")



def operations(actual, number, operation):
    if operation == 1:
        return actual + number
    elif operation == 2:
        return actual -  number
    elif operation == 3:
        return actual * number
    elif operation == 4:
        if operation != 0:
            return actual / number
        else:
            return "It cannot be divided into zero"



def calculator():
    print("Welcome to the calculator")
    actual = get_numbers()

    while True:
        operation = get_operations()

        if operation == 6:
            break
        elif operation == 5:
            actual = 0
            print("The result has been cleared")
            continue

        number = get_numbers()
        result   = operations(actual, number, operation)

        if isinstance(result , str):
            print(result)
        else:
            actual = result
            print(f"The result is: {actual}")

    print("Thank you for using the calculator")



calculator()