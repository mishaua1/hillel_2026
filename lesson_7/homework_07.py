# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1
    while True:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(3)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add_two_numbers(first_number, second_number):
    total = first_number + second_number
    return total

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total = total + number
    average = total / len(numbers)
    return average

print(calculate_average([10, 20, 30]))
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    return text[::-1]

print(reverse_string("hello"))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_word(words):
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(find_longest_word(["cat", "elephant", "dog"]))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1
    while True:
        result = number * multiplier
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(3)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add_two_numbers(first_number, second_number):
    total = first_number + second_number
    return total

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):
    total = 0
    for number in numbers:
        total = total + number
    average = total / len(numbers)
    return average

print(calculate_average([10, 20, 30]))
# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    return text[::-1]

print(reverse_string("hello"))
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_word(words):
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(find_longest_word(["cat", "elephant", "dog"]))


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# Функція 1 — підрахунок унікальних символів (ДЗ 6.1)
def count_unique_characters(text):
    """Повертає кількість унікальних символів у рядку."""
    return len(set(text))

print(count_unique_characters("hello"))  # 4


# Функція 2 — перевірка чи є літера 'h' у слові (ДЗ 6.2)
def has_letter_h(word):
    """Повертає True якщо слово містить літеру h."""
    return "h" in word.lower()

print(has_letter_h("Python"))  # True
print(has_letter_h("cat"))     # False


# Функція 3 — фільтрація рядків зі списку (ДЗ 6.3)
def filter_strings(lst):
    """Повертає список лише з рядків."""
    result = []
    for item in lst:
        if isinstance(item, str):
            result.append(item)
    return result

print(filter_strings(['1', 2, True, 'Python', 9]))  # ['1', 'Python']


# Функція 4 — сума парних чисел (ДЗ 6.4)
def sum_even_numbers(lst):
    """Повертає суму парних чисел списку."""
    suma = 0
    for item in lst:
        if item % 2 == 0:
            suma = suma + item
    return suma

print(sum_even_numbers([1, 2, 3, 4, 5]))



