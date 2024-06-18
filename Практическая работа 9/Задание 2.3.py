# Ввод строки с помощью input()
words = input("Введите строку слов, разделенных пробелами: ")

# Разделение строки на слова с помощью split()
word_list = words.split()

# Инициализация переменной для хранения самого длинного слова
longest_word = ""

# Перебор слов в списке и поиск самого длинного
for word in word_list:
    if len(word) > len(longest_word):
        longest_word = word

# Вывод самого длинного слова
print("Самое длинное слово: ", longest_word)