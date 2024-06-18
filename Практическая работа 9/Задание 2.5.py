sentence = input("Введите ненормированную строку: ")

# Удаляем лишние пробелы в начале и в конце строки
sentence = sentence.strip()

# Разбиваем строку на слова, удаляем пустые элементы и объединяем слова с одним пробелом
normalized_sentence = ' '.join(filter(None, sentence.split(' ')))

print("Нормированная строка:", normalized_sentence)