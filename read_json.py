import json

# czytamy plik JSON
with open("employees.json", encoding="utf-8") as file:
    employees = json.load(file)

# wyświetl wszystkich pracowników
for employee in employees:
    print(employee)

# typy danych są już poprawne!
print(f"\nFirst employee: {employees[0]['name']}")
print(f"Type of salary: {type(employees[0]['salary'])}")

# dodajemy nowego pracownika
new_employee = {
    "name": "Zofia",
    "age": 29,
    "city": "Łódź",
    "salary": 6800
}

employees.append(new_employee)

# zapisujemy zaktualizowaną listę do nowego pliku
with open("employees_updated.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, ensure_ascii=False, indent=4)

print("File employees_updated.json created!")