# Ćwiczenie 1
# Stwórz klasę Movie z atrybutami:
# title
# director
# year
# rating
class Movie:
    def __init__(self, title, director, year, rating):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating
# Dodaj metody:
# __str__ — zwraca "Title (year) - directed by director"
# is_recommended() — zwraca True jeśli rating >= 7
    def __str__(self):
        return f"{self.title} ({self.year}) - directed by {self.director}"

    def is_recommended(self):
        return self.rating >= 7