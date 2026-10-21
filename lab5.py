def find_words_with_max_unique_chars(s: str) -> str:
    word: str = ""
    max_unique: int = 0
    result: str = ""

    for ch in s + " ":
        if ch not in " ,.!?;:-":
            word += ch
        elif word:
            unique_count: int = len(set(word))
            if unique_count > max_unique:
                max_unique = unique_count
                result = word
            elif unique_count == max_unique:
                result += " " + word
            word = ""

    return result

if __name__ == "__main__":
    s: str = input("Введите строку: ")
    result = find_words_with_max_unique_chars(s)

    if result:
        print("Новая строка:", result)
    else:
        print("Подходящих слов нет")