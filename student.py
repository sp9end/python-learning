# Ćwiczenie 2
# Stwórz klasę Student z atrybutami:

# name
# grades — lista ocen (np. [4, 5, 3, 5, 4])

# Dodaj metody:

# average() — zwraca średnią ocen
# highest() — zwraca najwyższą ocenę
# lowest() — zwraca najniższą ocenę
# __str__ — zwraca "Student: name, Average: X.XX"



class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)
    
    def highest(self):
        return max(self.grades)
    
    def lowest(self):
        return min(self.grades)
    
    def __str__(self):
        return f"Student: {self.name}, Average: {self.average():.2f}"