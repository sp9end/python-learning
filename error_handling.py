# ten kod spowoduje błąd
# number = int("abc")  # ValueError
# print(10 / 0)        # ZeroDivisionError
# print([][5])         # IndexError
# print({}["key"])     # KeyError

# bez obsługi błędu — program się wysypuje
# number = int("abc")  # ValueError: invalid literal

# z obsługą błędu
try:
    number = int("abc")
    print(number)
except ValueError:
    print("Error: cannot convert to integer!")

print("Program continues...")

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: cannot divide by zero!")
        return None
    except TypeError:
        print("Error: both arguments must be numbers!")
        return None

print(divide(10, 2))   # 5.0
print(divide(10, 0))   # Error: cannot divide by zero!
print(divide(10, "a")) # Error: both arguments must be numbers!

# finally — wykona się zawsze
try:
    file = open("nonexistent.txt")
    content = file.read()
except FileNotFoundError:
    print("Error: file not found!")
finally:
    print("This always runs!")