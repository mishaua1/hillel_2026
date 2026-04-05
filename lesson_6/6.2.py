while True:
    word = input("Введіть слово з літерою 'h': ")
    if "h" in word.lower():
        print("Слово прийнято")
        break
    print("Немає літери 'h'")