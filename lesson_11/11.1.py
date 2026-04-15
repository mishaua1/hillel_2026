def sum_numbers(text):
    numbers = text.split(',')
    total = 0
    for n in numbers:
        total = total + int(n)
    return total

strings = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for s in strings:
    try:
        print(sum_numbers(s))
    except ValueError:
        print("Не можу це зробити!")