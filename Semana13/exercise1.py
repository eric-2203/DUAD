def print_info(func):
    def wrapper(a , b):
        print(f"First value is: {a}")
        print(f"Second value is: {b}")
        result =  a + b
        print(f"Result is: {result}")

    return wrapper


@print_info
def addition(a, b):
    result = a + b
    print(f"Result is: {result}")

    return result


addition(1, 245)