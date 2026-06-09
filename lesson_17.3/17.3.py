#Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

#Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

#Реалізуйте ітератор для зворотного виведення елементів списку.
class ReverseIterator:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

#Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenRange:

    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

#Напишіть декоратор, який логує аргументи та результати викликаної функції.
import functools
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
)


def log_calls(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info("Виклик %s | args=%s kwargs=%s", func.__name__, args, kwargs)
        result = func(*args, **kwargs)
        logging.info("Результат %s → %s", func.__name__, result)
        return result

    return wrapper


#Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def handle_exceptions(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(
                "Помилка у %s (%s: %s)", func.__name__, type(e).__name__, e
            )
            return None

    return wrapper


if __name__ == "__main__":
    print("=== Генератор парних чисел до 10 ===")
    print(list(even_numbers(10)))

    print("\n=== Генератор Фібоначчі до 50 ===")
    print(list(fibonacci(50)))

    print("\n=== Зворотній ітератор ===")
    for item in ReverseIterator([1, 2, 3, 4, 5]):
        print(item, end=" ")
    print()

    print("\n=== Ітератор парних чисел до 12 ===")
    for num in EvenRange(12):
        print(num, end=" ")
    print()

    print("\n=== Декоратор логування ===")

    @log_calls
    def add(a, b):
        return a + b

    add(3, 7)

    print("\n=== Декоратор обробки винятків ===")

    @handle_exceptions
    def divide(a, b):
        return a / b

    print(divide(10, 2))
    print(divide(5, 0))