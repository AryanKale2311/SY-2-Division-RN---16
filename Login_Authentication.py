def login_required(func):
    def wrapper():
        print("=" * 45)
        print("        LOGIN AUTHENTICATION")
        print("=" * 45)

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        print("-" * 45)

        if username == "admin" and password == "1234":
            print("#" * 45)
            print("      LOGIN SUCCESSFUL")
            print("#" * 45)
            func()
            print("#" * 45)
        else:
            print("#" * 45)
            print("  ACCESS DENIED!")
            print("Invalid Username or Password.")
            print("#" * 45)

    return wrapper


@login_required
def protected_page():
    print("Welcome! You have accessed the protected page.")
    print("=" * 45)
    print("       PROTECTED PAGE OPENED")
    print("=" * 45)


# Function Call
protected_page()