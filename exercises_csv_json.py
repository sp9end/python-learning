import csv
import json

# jedno wczytanie
books = []
with open("books.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        books.append({
            "title": row["title"],
            "author": row["author"],
            "year": int(row["year"]),
            "pages": int(row["pages"]),
            "rating": int(row["rating"])
        })

# ćwiczenie 1 - książki z oceną powyżej 7
print("--- Books rated above 7 ---")
for book in books:
    if book["rating"] > 7:
        print(f'{book["title"]} → rating: {book["rating"]}')

# ćwiczenie 2 - statystyki
ratings = [book["rating"] for book in books]
avg_rating = sum(ratings) / len(ratings)
best_book = max(books, key=lambda x: x["rating"])
worst_book = min(books, key=lambda x: x["rating"])

print(f"\nŚrednia ocena: {avg_rating:.2f}")
print(f"Najwyżej oceniona: {best_book['title']} → {best_book['rating']}")
print(f"Najniżej oceniona: {worst_book['title']} → {worst_book['rating']}")

# ćwiczenie 3 - zapis do JSON
with open("books.json", "w", encoding="utf-8") as json_file:
    json.dump(books, json_file, ensure_ascii=False, indent=4)

print("\nFile books.json created!")