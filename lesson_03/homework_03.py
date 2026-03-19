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
print(f"Площа Чорного моря становить {black_sea} км², а площа Азовського моря становить {azov_sea} км². Яку площу займають Чорне та Азовське моря разом?")

# task 05
total = 375291
first_second = 250449
second_third = 222950
print(f"Мережа супермаркетів має 3 склади, де всього розміщено {total} товарів. На першому та другому складах перебуває {first_second} товарів. На другому та третьому – {second_third} товарів. Знайдіть кількість товарів на кожному складі.")

# task 06
months = 18
payment = 1179
print(f"Сплачувати необхідно буде {months} місяців по {payment} грн/місяць. Обчисліть вартість комп'ютера.")

# task 07
a, b, c, d, e, f = 8019, 9907, 2789, 7248, 7128, 19224
print(f"Знайди остачу від ділення чисел: a) {a}:8, b) {b}:9, c) {c}:5, d) {d}:6, e) {e}:5, f) {f}:9")

# task 08
pizza_large, pizza_medium = 274, 218
juice, cake, water = 35, 350, 21
print(f"Піца велика - {pizza_large} грн, піца середня - {pizza_medium} грн, сік - {juice} грн, торт - {cake} грн, вода - {water} грн. Скільки грошей знадобиться?")

# task 09
photos = 232
per_page = 8
print(f"Ігор має {photos} фотографій. На одній сторінці може бути {per_page} фото. Скільки сторінок знадобиться?")

# task 10
distance = 1600
fuel_per_100 = 9
tank = 48
print(f"Відстань між містами становить {distance} км. На кожні 100 км необхідно {fuel_per_100} літрів бензину. Місткість баку становить {tank} літрів. Скільки літрів знадобиться і скільки разів треба заїхати на заправку?")