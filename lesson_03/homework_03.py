# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

# task 02 - знайти всі символи одинарної лапки
single_quotes = []
for char in alice_in_wonderland:
    if char == "'":
        single_quotes.append(char)

print("Одинарні лапки:", single_quotes)
print("Кількість:", len(single_quotes))

# task 03 - вивести змінну
print(alice_in_wonderland)

# task 04
black_sea = 436402
azov_sea = 37800
print(f"{black_sea + azov_sea} км²")

# task 05
total = 375291
first_second = 250449
second_third = 222950

third = total - first_second
second = second_third - third
first = first_second - second

print(first)
print(second)
print(third)

# task 06
months = 18
payment = 1179
print(f"{months * payment} грн")

# task 07
print(f"a) {8019 % 8}")
print(f"b) {9907 % 9}")
print(f"c) {2789 % 5}")
print(f"d) {7248 % 6}")
print(f"e) {7128 % 5}")
print(f"f) {19224 % 9}")

# task 08
pizza_large = 4 * 274
pizza_medium = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
total_birthday = pizza_large + pizza_medium + juice + cake + water
print(f"{total_birthday} грн")

# task 09
photos = 232
per_page = 8
pages = photos // per_page
if photos % per_page > 0:
    pages += 1
print(f"{pages}")

# task 10
distance = 1600
fuel_per_100 = 9
tank = 48
total_fuel = distance / 100 * fuel_per_100
stops = (total_fuel / tank)
print(f"Потрібно {total_fuel} літрів")
print(f"Зупинок: {stops}")