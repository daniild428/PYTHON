def count_words_starting_with_b(text):
    words = text.split()
    count = 0

    for word in words:
        if word.lower().startswith('b'):
            count += 1

    return count


# Пример использования функции
text = input("Введите предложение")
result = count_words_starting_with_b(text)
print(f"Количество слов, начинающихся с буквы 'b': {result}")
