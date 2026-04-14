# Ćwiczenie 1
# Stwórz listę 5 dowolnych miast. Wyświetl:
cities = ["Warszawa", "Opole", "Katowice", "Szczecin", "Gliwice"]
# pierwsze miasto
print(f"Pierwsze miasto: {cities[0]}")
# ostatnie miasto
print(f"Ostatnie miasto na liście: {cities[-1]}")
# liczbę miast na liście
print(f"Liczba miast: {len(cities)}")


# Ćwiczenie 2
# Masz listę temperatur z tygodnia:
temperatures = [18.5, 21.0, 19.3, 22.7, 20.1, 17.8, 23.4]
# Wyświetl:

# temperaturę z pierwszego dnia
print(f"Temperatura w pierwszym dniu: {temperatures[0]}")
# temperaturę z ostatniego dnia
print(f"Temperatura w ostatnim dniu: {temperatures[-1]}")
# liczbę pomiarów
print(f"Liczba pomiarów: {len(temperatures)}")
# czy temperatura 22.7 jest na liście
print(22.7 in temperatures)


# Ćwiczenie 3
# Zacznij od pustej listy:
shopping_list = []
# Dodaj do niej 4 dowolne produkty przez append(), a potem wyświetl całą listę i jej długość.
shopping_list.append("mleko")
shopping_list.append("ser")
shopping_list.append("jogurt")
shopping_list.append("banany")

print(shopping_list)
print(f"Długość listy zakupów: {len(shopping_list)}")