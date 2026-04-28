from datetime import date
from collections import Counter
import csv
import statistics as stats

# Ćwiczenie 1 — datetime
# Napisz program który:
today = date.today()

# wyświetla dzisiejszą datę w formacie "Today is: 28 April 2026"
print(f"Dzisiaj jest: {today.strftime("%d %B %Y")}")

# oblicza ile dni zostało do końca roku
year_end_date = date(2026, 12, 31)
days_until_year_end = (year_end_date - today).days
print(f"Do końca roku pozostało: {days_until_year_end} dni.")
# oblicza ile dni minęło od 1 stycznia 2026
january_first_date = date(2026,1,1)
days_since_january_first = (today - january_first_date).days + 1
print(f"Od 1 stycznia 2026 mineło: {days_since_january_first} dni.")

# Ćwiczenie 2 — collections
# Wczytaj books.csv i używając Counter znajdź:
authors = []
ratings = []
pages = []

with open("books.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        authors.append(row["author"])
        ratings.append(int(row["rating"]))
        pages.append(int(row["pages"]))
# ilu książek napisał każdy autor
author_counts = Counter(authors)

print("Liczba książek per autor:")
for author, count in author_counts.items():
    print(f"{author}: {count}")

# 5 najplodniejszych autorów w Twojej kolekcji
print("\nTop 5 najpłodniejszych autorów:")
for author, count in author_counts.most_common(5):
    print(f"{author}: {count}")


# Ćwiczenie 3 — statistics
# Używając modułu statistics i danych z books.csv oblicz:

# średnią ocenę wszystkich książek
# medianę ocen
# odchylenie standardowe ocen
# # średnią liczbę stron

# obliczenia
avg_rating = stats.mean(ratings)
median_rating = stats.median(ratings)
std_rating = stats.stdev(ratings)
avg_pages = stats.mean(pages)

print(f"Średnia ocena: {avg_rating:.2f}")
print(f"Mediana ocen: {median_rating}")
print(f"Odchylenie standardowe ocen: {std_rating:.2f}")
print(f"Średnia liczba stron: {avg_pages:.2f}")