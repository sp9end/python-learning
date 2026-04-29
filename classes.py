# definicja klasy
class Book:
    def __init__(self, title, author, year, pages, rating):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.rating = rating

    def __str__(self):
        return f'"{self.title}" by {self.author} ({self.year})'

    def describe(self):
        print(f'"{self.title}" by {self.author} → rating: {self.rating}')

    def is_recommended(self):
        return self.rating >= 8


# dostęp do atrybutów
book1 = Book("1984", "George Orwell", 1949, 328, 9)
book2 = Book("Diuna", "Frank Herbert", 1965, 604, 10)

print(book1.title)
print(book1.author)
print(book2.rating)

# describe() i is_recommended()
book1.describe()
book3 = Book("Pięćdziesiąt twarzy Greya", "E.L. James", 2011, 514, 4)
book3.describe()

print(book1.is_recommended())  # True
print(book3.is_recommended())  # False

# lista obiektów
books = [
    Book("1984", "George Orwell", 1949, 328, 9),
    Book("Diuna", "Frank Herbert", 1965, 604, 10),
    Book("Pięćdziesiąt twarzy Greya", "E.L. James", 2011, 514, 4),
    Book("Mistrz i Małgorzata", "Michaił Bułhakow", 1967, 480, 10),
]

# wyświetl wszystkie
for book in books:
    print(book)

# tylko polecane
print("\nRecommended books:")
for book in books:
    if book.is_recommended():
        print(book)

# sortowanie po ocenie
sorted_books = sorted(books, key=lambda b: b.rating, reverse=True)
print("\nSorted by rating:")
for book in sorted_books:
    print(f"{book} → {book.rating}")