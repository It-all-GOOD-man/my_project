import random
import string
from collections import Counter

def print_menu():
    print("\n" + "="*60)
    print("ЛАБОРАТОРНАЯ РАБОТА 2 - ОСНОВЫ ПРОГРАММИРОВАНИЯ")
    print("="*60)
    print("ЦИКЛЫ:")
    print("1. Таблица умножения")
    print("2. Сумма нечётных чисел от 1 до 100")
    print("3. Делители числа")
    print("4. Факториал числа")
    print("5. Последовательность Фибоначчи")
    
    print("\nСПИСКИ:")
    print("6. Чётные элементы списка")
    print("7. Максимальное и минимальное число в списке")
    print("8. Сортировка пользовательских чисел")
    print("9. Удаление дубликатов из списка")
    print("10. Поменять местами первый и последний элемент")
    
    print("\nСЛОВАРИ:")
    print("11. Средний балл студентов")
    print("12. Количество каждой буквы в строке")
    print("13. Квадраты чисел")
    print("14. Словарь из двух списков")
    
    print("\nМНОЖЕСТВА:")
    print("15. Пересечение и объединение множеств")
    print("16. Уникальные слова в тексте")
    print("17. Общие элементы двух списков")
    print("18. Проверка подмножества")
    print("19. Удаление элементов меньше заданного числа")
    
    print("\nКОМБИНИРОВАННЫЕ ЗАДАНИЯ:")
    print("20. Уникальные случайные числа")
    print("21. Частота элементов в списке")
    print("22. Слова длиной больше 5 символов")
    print("23. Количество вхождений слов в предложении")
    print("24. Удаление дубликатов через множество")
    print("25. Самый дорогой товар")
    print("26. Частые имена")
    print("27. Первые вхождения символов")
    print("0. Выход")
    print("="*60)

def multiplication_table():
    print("\n--- Таблица умножения от 1 до 9 ---")
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i}×{j}={i*j:2}", end="\t")
        print()

def sum_odd_numbers():
    print("\n--- Сумма нечётных чисел от 1 до 100 ---")
    total = sum(i for i in range(1, 101) if i % 2 != 0)
    print(f"Сумма: {total}")

def find_divisors():
    print("\n--- Поиск делителей числа ---")
    try:
        num = int(input("Введите число: "))
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        print(f"Делители числа {num}: {divisors}")
    except ValueError:
        print("Ошибка: введите целое число!")

def factorial():
    print("\n--- Вычисление факториала ---")
    try:
        num = int(input("Введите число: "))
        if num < 0:
            print("Факториал отрицательного числа не определен!")
            return
        
        result = 1
        for i in range(1, num + 1):
            result *= i
        
        print(f"{num}! = {result}")
    except ValueError:
        print("Ошибка: введите целое число!")

def fibonacci():
    print("\n--- Последовательность Фибоначчи ---")
    try:
        n = int(input("Введите длину последовательности: "))
        if n <= 0:
            print("Длина должна быть положительным числом!")
            return
        
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        
        print(f"Первые {n} чисел Фибоначчи: {fib[:n]}")
    except ValueError:
        print("Ошибка: введите целое число!")

def even_elements():
    print("\n--- Чётные элементы списка ---")
    numbers = [random.randint(-59, 50) for _ in range(10)]
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Исходный список: {numbers}")
    print(f"Чётные элементы: {even_numbers}")

def min_max_list():
    print("\n--- Максимальное и минимальное число в списке ---")
    numbers = [random.randint(-59, 50) for _ in range(10)]
    print(f"Список: {numbers}")
    print(f"Минимальное: {min(numbers)}")
    print(f"Максимальное: {max(numbers)}")

def sort_user_numbers():
    print("\n--- Сортировка пользовательских чисел ---")
    numbers = []
    for i in range(5):
        try:
            num = float(input(f"Введите число {i+1}: "))
            numbers.append(num)
        except ValueError:
            print("Ошибка: введите число!")
            return
    
    numbers.sort()
    print(f"Отсортированный список: {numbers}")

def remove_duplicates():
    print("\n--- Удаление дубликатов из списка ---")
    numbers = [random.randint(1, 10) for _ in range(15)]
    unique_numbers = []
    
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    
    print(f"Исходный список: {numbers}")
    print(f"Без дубликатов: {unique_numbers}")

def swap_first_last():
    print("\n--- Поменять местами первый и последний элемент ---")
    numbers = [random.randint(-59, 50) for _ in range(10)]
    print(f"Исходный список: {numbers}")
    
    if len(numbers) >= 2:
        numbers[0], numbers[-1] = numbers[-1], numbers[0]
        print(f"После замены: {numbers}")
    else:
        print("Список слишком короткий для замены!")

def student_grades():
    print("\n--- Средний балл студентов ---")
    students = {
        "Иванов": 4.5,
        "Петров": 3.8,
        "Сидоров": 4.2,
        "Кузнецов": 4.8,
        "Смирнов": 3.9
    }
    
    print("Оценки студентов:")
    for student, grade in students.items():
        print(f"{student}: {grade}")
    
    average = sum(students.values()) / len(students)
    print(f"Средний балл: {average:.2f}")

def count_letters():
    print("\n--- Количество каждой буквы в строке ---")
    text = input("Введите строку: ").lower()
    letter_count = {}
    
    for char in text:
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1
    
    print("Количество букв:")
    for letter, count in sorted(letter_count.items()):
        print(f"{letter}: {count}")

def squares_dict():
    print("\n--- Квадраты чисел от 1 до 10 ---")
    squares = {i: i*i for i in range(1, 11)}
    for num, square in squares.items():
        print(f"{num}² = {square}")

def dict_from_lists():
    print("\n--- Словарь из двух списков ---")
    keys = ["имя", "возраст", "город", "профессия"]
    values = ["Анна", 25, "Москва", "инженер"]
    
    result_dict = dict(zip(keys, values))
    print("Ключи:", keys)
    print("Значения:", values)
    print("Результирующий словарь:", result_dict)

def set_operations():
    print("\n--- Операции с множествами ---")
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print(f"Множество 1: {set1}")
    print(f"Множество 2: {set2}")
    print(f"Пересечение: {set1 & set2}")
    print(f"Объединение: {set1 | set2}")

def unique_words():
    print("\n--- Уникальные слова в тексте ---")
    text = input("Введите текст: ").lower()
    words = text.split()
    unique_words_set = set(words)
    
    print(f"Все слова: {words}")
    print(f"Уникальные слова: {sorted(unique_words_set)}")

def common_elements():
    print("\n--- Общие элементы двух списков ---")
    list1 = [random.randint(1, 10) for _ in range(8)]
    list2 = [random.randint(1, 10) for _ in range(8)]
    
    common = set(list1) & set(list2)
    print(f"Список 1: {list1}")
    print(f"Список 2: {list2}")
    print(f"Общие элементы: {common}")

def check_subset():
    print("\n--- Проверка подмножества ---")
    set1 = {1, 2, 3, 4, 5}
    set2 = {2, 3, 4}
    
    print(f"Множество 1: {set1}")
    print(f"Множество 2: {set2}")
    print(f"set2 является подмножеством set1: {set2.issubset(set1)}")

def remove_small_elements():
    print("\n--- Удаление элементов меньше заданного числа ---")
    numbers_set = {random.randint(1, 20) for _ in range(10)}
    print(f"Исходное множество: {numbers_set}")
    
    try:
        threshold = int(input("Введите пороговое число: "))
        numbers_set = {x for x in numbers_set if x >= threshold}
        print(f"Результат: {numbers_set}")
    except ValueError:
        print("Ошибка: введите целое число!")

def unique_random_numbers():
    print("\n--- Уникальные случайные числа ---")
    numbers = [random.randint(1, 20) for _ in range(20)]
    unique_numbers = list(set(numbers))
    
    print(f"Исходный список: {numbers}")
    print(f"Уникальные значения: {unique_numbers}")

def element_frequency():
    print("\n--- Частота элементов в списке ---")
    numbers = [random.randint(1, 10) for _ in range(15)]
    frequency = {}
    
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    print(f"Список: {numbers}")
    print("Частота элементов:")
    for num, count in frequency.items():
        print(f"{num}: {count}")

def long_words():
    print("\n--- Слова длиной больше 5 символов ---")
    words = ["программирование", "python", "код", "алгоритм", "структура", "данные", "цикл", "функция"]
    long_words_set = {word for word in words if len(word) > 5}
    
    print(f"Все слова: {words}")
    print(f"Слова длиной > 5: {long_words_set}")

def word_count():
    print("\n--- Количество вхождений слов в предложении ---")
    sentence = input("Введите предложение: ").lower()
    words = sentence.split()
    word_count = {}
    
    for word in words:
        word = word.strip('.,!?;:')
        word_count[word] = word_count.get(word, 0) + 1
    
    print("Количество вхождений слов:")
    for word, count in word_count.items():
        print(f"'{word}': {count}")

def remove_dups_via_set():
    print("\n--- Удаление дубликатов через множество ---")
    numbers = [random.randint(1, 10) for _ in range(15)]
    unique_numbers = list(set(numbers))
    
    print(f"Исходный список: {numbers}")
    print(f"Без дубликатов: {unique_numbers}")

def most_expensive():
    print("\n--- Самый дорогой товар ---")
    products = {
        "хлеб": 50,
        "молоко": 80,
        "сыр": 300,
        "мясо": 500,
        "рыба": 400
    }
    
    print("Товары и цены:")
    for product, price in products.items():
        print(f"{product}: {price} руб.")
    
    most_expensive = max(products, key=products.get)
    print(f"Самый дорогой товар: {most_expensive} ({products[most_expensive]} руб.)")

def frequent_names():
    print("\n--- Частые имена ---")
    names = ["анна", "иван", "мария", "иван", "петр", "анна", "анна", "мария"]
    name_count = Counter(names)
    
    print(f"Список имён: {names}")
    print("Количество повторений:")
    for name, count in name_count.items():
        print(f"{name}: {count}")
    
    duplicates = [name for name, count in name_count.items() if count > 1]
    most_common = name_count.most_common(1)[0]
    
    print(f"Имена с повторениями: {duplicates}")
    print(f"Самое частое имя: '{most_common[0]}' ({most_common[1]} раз(а))")

def first_occurrence():
    print("\n--- Первые вхождения символов ---")
    text = input("Введите строку: ")
    first_occurrence_dict = {}
    
    for index, char in enumerate(text):
        if char not in first_occurrence_dict:
            first_occurrence_dict[char] = index
    
    print("Первые вхождения символов:")
    for char, index in first_occurrence_dict.items():
        print(f"'{char}': позиция {index}")

def main():
    while True:
        print_menu()
        
        try:
            choice = int(input("\nВыберите задание (0-27): "))
            
            if choice == 0:
                print("Выход из программы...")
                break
            
            functions = {
                1: multiplication_table,
                2: sum_odd_numbers,
                3: find_divisors,
                4: factorial,
                5: fibonacci,
                6: even_elements,
                7: min_max_list,
                8: sort_user_numbers,
                9: remove_duplicates,
                10: swap_first_last,
                11: student_grades,
                12: count_letters,
                13: squares_dict,
                14: dict_from_lists,
                15: set_operations,
                16: unique_words,
                17: common_elements,
                18: check_subset,
                19: remove_small_elements,
                20: unique_random_numbers,
                21: element_frequency,
                22: long_words,
                23: word_count,
                24: remove_dups_via_set,
                25: most_expensive,
                26: frequent_names,
                27: first_occurrence
            }
            
            if choice in functions:
                functions[choice]()
            else:
                print("Неверный выбор! Попробуйте снова.")
            
            input("\nНажмите Enter для продолжения...")
            
        except ValueError:
            print("Ошибка: введите число от 0 до 27!")
        except KeyboardInterrupt:
            print("\n\nПрограмма прервана пользователем.")
            break

if __name__ == "__main__":
    main()