# Задание 1

print([i**2 for i in range(1, 11)])

# Задание 2

print([i for i in range(2, 21, 2)])

# Задание 3

words = ["python", "Java", "C++", "Rust", "go"]
print([i for i in words if i[0].isupper() and len(i)>3])