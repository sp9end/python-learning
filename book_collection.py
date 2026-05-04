# Stwórz klasę BookCollection która:

# ma atrybut books — pusta lista w __init__
# metodę add_book(title, author, rating) — dodaje nową książkę do listy
# metodę best_book() — zwraca książkę z najwyższą oceną
# metodę count() — zwraca liczbę książek w kolekcji


class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, rating):
        self.books.append({
            "title": title,
            "author": author,
            "rating": rating
        })
    
    def best_book(self):
        return max(self.books, key=lambda b: b["rating"])
    
    def count(self):
        return len(self.books)