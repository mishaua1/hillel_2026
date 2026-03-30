s = input()

unique = []
for char in s:
    if char not in unique:
        unique.append(char)

print(len(unique) > 10)