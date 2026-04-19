# Ćwiczenie 1
# Napisz funkcję celsius_to_fahrenheit(celsius) która przyjmuje temperaturę w Celsjuszach i zwraca temperaturę w Fahrenheitach.
# Przetestuj ją dla wartości: 0, 100, 37, -40

# 💡 Wzór: F = (C × 9/5) + 32
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(37))
print(celsius_to_fahrenheit(-40))

# Ćwiczenie 2
# Napisz funkcję describe_city(**kwargs) która przyjmuje dowolne informacje o mieście i wyświetla je w formacie:
# City report:
# name: Warszawa
# population: 1800000
# ...

def describe_city(**kwargs):
    print("City report:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
describe_city(name="Warszawa", population=1800000, country="Poland")
describe_city(name="Kraków", population=1300000, country="Poland")


# Ćwiczenie 3
# Napisz funkcję calculate_stats(*args) która przyjmuje dowolną liczbę liczb i wyświetla:

# ile liczb podano
# sumę
# najmniejszą liczbę
# największą liczbę
def calculate_stats(*args):
    print(f"Count: {len(args)}")
    print(f"Sum: {sum(args)}")
    print(f"Min: {min(args)}")
    print(f"Max: {max(args)}")

calculate_stats(1,1,2,2)
calculate_stats(5,5)