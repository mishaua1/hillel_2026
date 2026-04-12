# ДЗ 5
def check_age(lst, indexes, min_age):
    return all(lst[i][2] >= min_age for i in indexes)

# ДЗ 6.2
def contains_h(word):
    return "h" in word.lower()

# ДЗ 6.3
def filter_strings(lst):
    result = []
    for item in lst:
        if isinstance(item, str):
            result.append(item)
    return result

# ДЗ 6.4
def sum_even(lst):
    total = 0
    for item in lst:
        if item % 2 == 0:
            total += item
    return total