# Ćwiczenie 1
# Masz listę temperatur w Celsjuszach:

celsius = [0, 10, 20, 30, 37, 100]

# Używając list comprehension stwórz nową listę z temperaturami w Fahrenheitach.
fahrenheit = [(c * 9/5) + 32 for c in celsius]

print(fahrenheit)

# Ćwiczenie 2
# Masz listę wyników egzaminów:
scores = [45, 72, 88, 53, 91, 67, 39, 84, 76, 55]
# Używając list comprehension stwórz dwie nowe listy:

# passing — tylko wyniki większe lub równe 60
passing = [p for p in scores if p >= 60]

# failing — tylko wyniki poniżej 60
failing = [f for f in scores if f < 60]

# Wyświetl obie listy i ich długości.
print(passing)
print(len(passing))
print(failing)
print(len(failing))

# Ćwiczenie 3
# Masz listę słów:
words = ["python", "data", "analyst", "code", "list", "comprehension"]
# Używając list comprehension stwórz nową listę zawierającą długości każdego słowa.
lengths = [len(word) for word in words]

# Wyświetl obie listy razem tak żeby było widać słowo i jego długość:
# python → 6
# data → 4
# ...
for word, length in zip(words, lengths):
    print(f"{word} → {length}")
