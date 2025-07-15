

def check_numbers(func):
    def wrapper(*args):
        for value in args:
            if isinstance(value, int) == False:
                raise ValueError(
                    "Invalid value. Values need to be numbers"
                )
        func(*args)
        
        

    return wrapper


@check_numbers
def add_numbers(*args):
    result = sum(args)
    print(f"The result is {result}")

    return result

add_numbers(1, 2, 252, 63)