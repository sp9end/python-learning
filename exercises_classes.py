from movie import Movie
from student import Student
from book_collection import BookCollection

# Ćwiczenie 1
# Stwórz 4 obiekty i wyświetl tylko polecane filmy.
# --- tworzymy obiekty ---
m1 = Movie("Inception", "Christopher Nolan", 2010, 9)
m2 = Movie("The Room", "Tommy Wiseau", 2003, 3)
m3 = Movie("Interstellar", "Christopher Nolan", 2014, 8)
m4 = Movie("Twilight", "Catherine Hardwicke", 2008, 5)

movies = [m1, m2, m3, m4]

for movie in movies:
    if movie.is_recommended():
        print(movie)

# Ćwiczenie 2
# Stwórz 4 studentów i wyświetl ich statystyki.
# --- tworzymy obiekty ---
s1 = Student("Anna", [4, 5, 3, 5, 4])
s2 = Student("Bartek", [2, 3, 3, 4])
s3 = Student("Karolina", [5, 5, 5, 4, 5])
s4 = Student("Marek", [3, 2, 2, 3])

students = [s1, s2, s3, s4]

# --- wyświetlamy wszystkich ---
for student in students:
    print(student)

# Ćwiczenie 3
# Dodaj 5 książek i wyświetl najlepszą oraz liczbę wszystkich.
collection = BookCollection()

collection.add_book("Inception of Data", "Alice Brown", 9)
collection.add_book("Python Mastery", "John Smith", 8)
collection.add_book("Deep Learning 101", "Sarah Lee", 7)
collection.add_book("The Bug Hunter", "Mark Davis", 6)
collection.add_book("Clean Code", "Robert C. Martin", 10)

best = collection.best_book()

print("Najlepsza książka:")
print(f"{best['title']} — {best['author']} (rating: {best['rating']})")

print("\nLiczba wszystkich książek:", collection.count())
