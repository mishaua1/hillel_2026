# Функція 1 — підрахунок унікальних символів (ДЗ 6.1)
def count_unique_characters(text):
    """Повертає кількість унікальних символів у рядку."""
    return len(set(text))

print(count_unique_characters("hello"))  # 4