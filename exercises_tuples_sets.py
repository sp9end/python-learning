# Ćwiczenie 1
# Stwórz krotkę z miesiącami roku (wszystkie 12). Wyświetl:
months = ("styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień")
# pierwszy miesiąc
print(f"Pierwszy miesiąc: {months[0]}")
# ostatni miesiąc
print(f"Ostatni miesiąc: {months[-1]}")
# liczbę miesięcy
print(f"Liczba miesięcy: {len(months)}")


# Ćwiczenie 2
# Masz listę z duplikatami:
visits = ["Warszawa", "Kraków", "Warszawa", "Gdańsk", "Kraków", "Warszawa", "Poznań"]

# zamień listę na zbiór żeby usunąć duplikaty
set_visits = set(visits)
# wyświetl zbiór
print(set_visits)
# wyświetl ile unikalnych miast odwiedzono
print(f"Mamy {len(set_visits)} unikalnych miast, które odwiedzono.")

# Ćwiczenie 3
# Stwórz krotkę z 3 Twoimi ulubionymi kolorami. Następnie stwórz zbiór z tych samych kolorów. Wyświetl oba i ich długości.
favorite_colors = ("red", "blue", "black")
set_favorite_colors = set(favorite_colors)

print(favorite_colors)
print(set_favorite_colors)

print(f"Długość krotki: {len(favorite_colors)}")
print(f"Długość zbioru: {len(set_favorite_colors)}")