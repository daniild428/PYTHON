def count_words_in_string(s):

    words = s[:-1].split()
    return len(words)


s = input("Введите предложение")
word_count = count_words_in_string(s)
print("Количество слов в строке:", word_count)