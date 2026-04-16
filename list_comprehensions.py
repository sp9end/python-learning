#zwykła pętla
numbers1 = [1, 2, 3, 4, 5]
squares1 = []

for n in numbers1:
    squares1.append(n ** 2)

print(squares1)

# To samo jako list comprehension:
numbers2 = [1, 2, 3, 4, 5]
squares2 = [n ** 2 for n in numbers2]

print(squares2)  # [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# tylko parzyste liczby
even = [n for n in numbers if n % 2 == 0]
print(even)  # [2, 4, 6, 8, 10]

# tylko liczby większe niż 5
greater = [n for n in numbers if n > 5]
print(greater)  # [6, 7, 8, 9, 10]

fruits = ["apple", "banana", "cherry", "date"]

# zamień wszystkie na wielkie litery
upper = [fruit.upper() for fruit in fruits]
print(upper)  # ['APPLE', 'BANANA', 'CHERRY', 'DATE']

# tylko owoce których nazwa ma więcej niż 5 liter
long_names = [fruit for fruit in fruits if len(fruit) > 5]
print(long_names)  # ['banana', 'cherry']