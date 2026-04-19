# ДЗ 5
def check_age(lst, indexes, min_age):
    if not isinstance(lst, list):
        raise TypeError("lst має бути списком!")
    return all(lst[i][2] >= min_age for i in indexes)

# ДЗ 6.2
def contains_h(word):
    if not isinstance(word, str):
        raise TypeError("word має бути рядком!")
    return "h" in word.lower()

# ДЗ 6.3
def filter_strings(lst):
    if not isinstance(lst, list):
        raise TypeError("lst має бути списком!")
    result = []
    for item in lst:
        if isinstance(item, str):
            result.append(item)
    return result

# ДЗ 6.4
def sum_even(lst):
    if not isinstance(lst, list):
        raise TypeError("lst має бути списком!")
    total = 0
    for item in lst:
        if item % 2 == 0:
            total += item
    return total