# Exceptions - try / except / Exception

# Basic try/except
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("No exceptions occurred.")
finally:
    print("This always runs.")


# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age


# Custom exception
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(e)
