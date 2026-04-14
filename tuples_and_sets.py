coordinates = (52.2297, 21.0122)  # szerokość i długość geograficzna Warszawy
rgb_color = (255, 128, 0)
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print(coordinates[0])    # 52.2297
print(coordinates[1])    # 21.0122
print(len(days_of_week)) # 7

unique_cities = {"Warszawa", "Kraków", "Gdańsk", "Warszawa", "Kraków"}
print(unique_cities)  # {'Gdańsk', 'Kraków', 'Warszawa'} ← duplikaty zniknęły!

numbers = {3, 1, 4, 1, 5, 9, 2, 6, 5}
print(numbers)  # {1, 2, 3, 4, 5, 6, 9} ← tylko unikalne, bez kolejności!

# dodanie elementu
unique_cities.add("Wrocław")
print(unique_cities)

# sprawdzenie czy element istnieje (bardzo szybkie!)
print("Kraków" in unique_cities)   # True
print("Poznań" in unique_cities)   # False