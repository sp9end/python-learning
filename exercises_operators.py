# Ćwiczenie 1

# Masz dane o sklepie:
price = 24.99
quantity = 7
discount = 0.1  # 10% zniżki

# Oblicz i wyświetl:
# całkowitą wartość zamówienia (cena × ilość)

order_value = price * quantity
print(f"Wartość zamówienia: {order_value:.2f} zł.")
# wartość po zniżce
value_after_discount = order_value - (order_value * discount)
print(f"Zniżka: {discount * 100} %. Wartość po zniżce: {value_after_discount:.2f} zł.")

# Ćwiczenie 2
# Masz liczbę seconds = 9385. Oblicz i wyświetl:
seconds = 9385

# pełne godziny
hours = seconds // 3600

# ile sekund zostaje po odjęciu godzin
remaining_seconds = seconds % 3600

# pełne minuty z pozostałych sekund
minutes = remaining_seconds // 60

# ile sekund zostaje na końcu
final_seconds = remaining_seconds % 60

print("Godziny:", hours)
print("Minuty:", minutes)
print("Sekundy:", final_seconds)

# Ćwiczenie 3
# Masz dane dwóch pracowników:
employee1_salary = 5400
employee2_salary = 6200
# Wyświetl wyniki tych porównań:

# czy employee1 zarabia więcej niż employee2
print(employee1_salary > employee2_salary)
# czy zarobki są równe
print(employee1_salary == employee2_salary)
# czy employee1 zarabia co najmniej 5000
print(employee1_salary >= 5000)