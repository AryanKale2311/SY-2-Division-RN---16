# Decorator to check if all arguments are positive integers

def validate_input(func):
    def wrapper(*args):
        print("-" * 45)
        print("      INPUT VALIDATION")
        print("-" * 45)

        for i in args:
            if type(i) != int or i <= 0:
                print("Error: All arguments must be positive integers.")
                print("-" * 45)
                return

        func(*args)
        print("-" * 45)

    return wrapper


@validate_input
def multiply(a, b):
    print("Multiplication =", a * b)


# Function Calls
multiply(5, 4)
multiply(-2, 6)
multiply(3.5, 2)