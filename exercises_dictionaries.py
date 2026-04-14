# Ćwiczenie 1
# Stwórz słownik opisujący książkę:
# tytuł
# autor
# rok wydania
# liczba stron
# czy już przeczytana (True/False)

# Wyświetl każdą wartość osobno przez klucz.

book_data = {"title": "Kicia Kocia ratuje boisko",
             "author": "Anita Głowińska",
             "year_release": 2026,
             "number_pages": 24,
             "read": True
             }

print(book_data["title"])
print(book_data["author"])
print(book_data["year_release"])
print(book_data["number_pages"])
print(book_data["read"])

# Ćwiczenie 2
# Masz słownik z cenami produktów:
prices = {
    "milk": 3.49,
    "bread": 4.99,
    "butter": 8.79,
    "eggs": 12.99
}

# dodaj nowy produkt "cheese" z ceną 15.49
prices["cheese"] = 15.49

# zmień cenę "milk" na 3.99
prices["milk"] = 3.99

# usuń "butter" ze słownika
del prices["butter"]

# wyświetl końcowy słownik
print(prices)

# Ćwiczenie 3
# Stwórz słownik opisujący siebie jako kandydatkę do pracy:
# imię
# zawód (np. "data analyst")
# umiejętności — jako lista wartości!
# lata doświadczenia

job_candidate = {"name": "Barbara",
                 "occupation": "data analyst",
                 "skills": ["sql", "python", "vs code", "excel / google sheets", "power bi"],
                "years_experience": 3}


# Wyświetl cały słownik oraz samą listę umiejętności.
print(job_candidate)
print(job_candidate["skills"])