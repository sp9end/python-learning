fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Basia", 39, 1.70, True]  # lista może mieć różne typy!

fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple   ← pierwszy element, indeks 0!
print(fruits[1])   # banana
print(fruits[2])   # cherry
print(fruits[-1])  # cherry  ← ostatni element
print(fruits[-2])  # banana  ← przedostatni element

fruits = ["apple", "banana", "cherry"]

# długość listy
print(len(fruits))        # 3

# dodanie elementu na koniec
fruits.append("orange")
print(fruits)             # ["apple", "banana", "cherry", "orange"]

# usunięcie elementu
fruits.remove("banana")
print(fruits)             # ["apple", "cherry", "orange"]

# sprawdzenie czy element jest w liście
print("apple" in fruits)  # True
print("banana" in fruits) # False