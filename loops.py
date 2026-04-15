fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# wyświetl liczby od 0 do 4
for i in range(5):
    print(i)

# wyświetl liczby od 1 do 5
for i in range(1,6):
    print(i)

# wyświetl liczby od 0 do 10 co 2
for i in range(0,11, 2):
    print(i)

# pętle po słowniku
person = {
    "name": "Basia",
    "age": 39,
    "city": "Warszawa"
}

for key, value in person.items():
    print(f"{key}: {value}")

# pętla while
counter = 0

while counter < 5:
    print(f"Counter: {counter}")
    counter += 1
print("Done!") 