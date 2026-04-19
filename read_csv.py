import csv

employees = []

with open("employees.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        employees.append({
            "name": row["name"],
            "age": int(row["age"]),
            "city": row["city"],
            "salary": float(row["salary"])
        })

# wyświetl wszystkich pracowników
for employee in employees:
    print(employee)

# oblicz średnią pensję
total_salary = sum(e["salary"] for e in employees)
avg_salary = total_salary / len(employees)
print(f"\nAverage salary: {avg_salary:.2f} PLN")

# zapisujemy tylko pracowników z pensją powyżej średniej
with open("high_earners.csv", "w", encoding="utf-8", newline="") as file:
    fieldnames = ["name", "age", "city", "salary"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    for employee in employees:
        if employee["salary"] > avg_salary:
            writer.writerow(employee)

print("File high_earners.csv created!")