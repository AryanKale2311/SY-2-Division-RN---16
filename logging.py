# Decorator for Function Call Logging

def log_function(func):
    def wrapper():
        print("=" * 50)
        print("          FUNCTION CALL LOGGER")
        print("=" * 50)

        current_time = input("Enter Current Time (HH:MM:SS): ")

        print("-" * 50)
        print("Function Name :", func.__name__)
        print("Called At     :", current_time)
        print("-" * 50)

        func()

        print("#" * 50)
        print("     FUNCTION EXECUTED SUCCESSFULLY")
        print("#" * 50)

    return wrapper


@log_function
def display_message():
    print("Hello! This function has been executed.")


# Function Call
display_message()