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