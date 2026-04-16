# Ćwiczenie 1
# Masz listę temperatur:
temperatures = [18.5, 21.0, 19.3, 22.7, 20.1, 17.8, 23.4]
# Używając pętli for wyświetl każdą temperaturę w formacie:
# Day 1: 18.5°C
# Day 2: 21.0°C
# ...
for index, value in enumerate(temperatures, start=1):
    print(f"Day {index}: {value}")


# Ćwiczenie 2
# Używając pętli for i range() wyświetl tabliczkę mnożenia dla liczby 7 (od 7×1 do 7×10) w formacie:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
print("Tabliczka mnożenia dla liczby 7")
for i in range(1, 11):
    print(7, "x", i, "=", 7 *i )


# Ćwiczenie 3
# Używając pętli while zsumuj wszystkie liczby od 1 do 100 i wyświetl wynik.

# 💡 Wskazówka: Zacznij od total = 0 i dodawaj kolejne liczby w każdym obrocie pętli.
i = 1
total = 0
while i < 101:
    total += i
    i += 1
print(f"Zsumowanie liczb od 1 do 100 daje wynik : {total}")

