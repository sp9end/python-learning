import os
from datetime import datetime, date
from collections import Counter
import statistics

# aktualny folder roboczy
print(os.getcwd())

# lista plików w folderze
files = os.listdir(".")
print(files)

# sprawdzenie czy plik istnieje
print(os.path.exists("books.csv")) # True
print(os.path.exists("test.csv")) # False

# rozmiar pliku w bajtach
size = os.path.getsize("books.csv")
print(f"books.csv size: {size} bytes")

# dzisiejsza data
today = date.today()
print(f"Today: {today}")

# aktualny czas
now = datetime.now()
print(f"Now: {now}")

# formatowanie daty
print(now.strftime("%d-%m-%Y"))        # 22-04-2026
print(now.strftime("%d %B %Y"))        # 22 April 2026
print(now.strftime("%H:%M:%S"))        # godzina:minuty:sekundy

# obliczenia na datach
from datetime import timedelta
tomorrow = today + timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

# różnica między datami
birthday = date(1986, 3, 15)
age_days = (today - birthday).days
print(f"Days since birthday: {age_days}")

# zliczanie wystąpień elementów
words = ["python", "data", "python", "analyst", "data", "python"]
counter = Counter(words)
print(counter)
# Counter({'python': 3, 'data': 2, 'analyst': 1})

# najczęściej występujące elementy
print(counter.most_common(2))
# [('python', 3), ('data', 2)]

# zliczanie liter w stringu
letters = Counter("hello world")
print(letters)

numbers = [18.5, 21.0, 19.3, 22.7, 20.1, 17.8, 23.4]

print(f"Mean: {statistics.mean(numbers):.2f}")
print(f"Median: {statistics.median(numbers):.2f}")
print(f"Mode: {statistics.mode([1, 2, 2, 3, 3, 3])}")
print(f"Stdev: {statistics.stdev(numbers):.2f}")
print(f"Variance: {statistics.variance(numbers):.2f}")