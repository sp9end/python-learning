# Ćwiczenie 1
# Napisz funkcję safe_divide(a, b) która:
# dzieli a przez b
# obsługuje ZeroDivisionError i TypeError
# zwraca wynik lub None w przypadku błędu

# Przetestuj dla: (10, 2), (10, 0), (10, "x"), (100, 4)

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: cannot divide by zero!")
        return None
    except TypeError:
        print("Error: both arguments must be numbers!")
        return None

print(safe_divide(10, 2))     # 5.0
print(safe_divide(10, 0))     # None
print(safe_divide(10, "x"))   # None
print(safe_divide(100, 4))    # 25.0

# Ćwiczenie 2
# Napisz funkcję read_file(filename) która:
# otwiera i czyta plik
# obsługuje FileNotFoundError
# w bloku finally wyświetla "Operation completed"
# zwraca zawartość pliku lub None jeśli plik nie istnieje

# Przetestuj dla: "books.csv" (istnieje) i "missing.csv" (nie istnieje)

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None
    finally:
        print("Operation completed")

print(read_file("books.csv"))   # plik istnieje
print(read_file("missing.csv")) # plik nie istnieje


# Ćwiczenie 3
# Napisz funkcję get_book_rating(books, index) która:

# przyjmuje listę książek i indeks
# zwraca ocenę książki pod tym indeksem
# obsługuje IndexError gdy indeks jest za duży
# obsługuje TypeError gdy indeks nie jest liczbą całkowitą

# Przetestuj dla poprawnego indeksu, za dużego indeksu i dla indeksu "abc".

def get_book_rating(books, index):
    try:
        return books[index]["rating"]
    except IndexError:
        return None
    except TypeError:
        return None

books = [
    {"title": "Book A", "rating": 8},
    {"title": "Book B", "rating": 6},
    {"title": "Book C", "rating": 9}
]

print(get_book_rating(books, 1))      # poprawny indeks
print(get_book_rating(books, 10))     # za duży indeks
print(get_book_rating(books, "abc"))  # indeks nie jest liczbą
