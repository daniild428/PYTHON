import string

sequence = input("Введите последовательность символов: ")


punctuation_set = set()
for char in sequence:
    if char in string.punctuation:
        punctuation_set.add(char)


print("Знаки арифметических операций и знаки препинания в последовательности:")
for char in punctuation_set:
    print(char, end=' ')