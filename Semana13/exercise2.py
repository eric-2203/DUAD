

def check_numbers(func):
    def wrapper(*args, **kwargs):
        for value in args:
            if isinstance(value, int) == False:
                raise ValueError(
                    "Invalid value. Values need to be numbers."
                )
        for value in kwargs:
            if isinstance(value, int) == False:
                raise ValueError("" \
                "Invalid value. Values need to be numbers.")
        func(*args, **kwargs)
        
        

    return wrapper


@check_numbers
def add_numbers(*args, **kwargs):
    result = sum(args) + sum(kwargs)
    print(f"The result is {result}")

    return result

add_numbers(1, 2, 252, 63, 10)