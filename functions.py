# definicja funkcji
def greet():
    print("Hello, World!")

# wywołanie funkcji
greet()  # Hello, World!
greet()  # Hello, World!
greet()  # Hello, World!

# Funkcja z argumentami
def greet(name):
    print(f"Hello, {name}!")

greet("Basia")    # Hello, Basia!
greet("Python")   # Hello, Python!

# Funkcja z wartością zwracaną
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
print(add(10, 20))  # 30

# Funkcja z domyślnym argumentem
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Basia")              # Hello, Basia!
greet("Basia", "Hi")        # Hi, Basia!
greet("Basia", "Cześć")     # Cześć, Basia!

# *args — dowolna liczba argumentów pozycyjnych
def add_all(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add_all(1, 2, 3))        # 6
print(add_all(1, 2, 3, 4, 5))  # 15
print(add_all(10, 20))         # 30

# **kwargs — dowolna liczba argumentów nazwanych
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Basia", age=39, city="Warszawa")
describe_person(name="Python", version=3.12)

def summary(title, *args, **kwargs):
    print(f"--- {title} ---")
    print(f"Numbers: {args}")
    print(f"Details: {kwargs}")

summary("Report", 1, 2, 3, author="Basia", year=2026)