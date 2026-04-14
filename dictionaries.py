person = {
    "name": "Basia",
    "age": 39,
    "city": "Warszawa"
}

print(person["name"])   # Basia
print(person["age"])    # 39
print(person["city"])   # Warszawa

# dodanie nowego klucza
person["job"] = "analyst"
print(person)

# zmiana wartości
person["age"] = 40
print(person["age"])    # 40

# usunięcie klucza
del person["city"]
print(person)

# sprawdzenie czy klucz istnieje
print("name" in person)   # True
print("city" in person)   # False

# lista kluczy
print(person.keys())

# lista wartości
print(person.values())
