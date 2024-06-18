
sequence = input("Введите последовательность символов: ")


elements_set = set()


for char in sequence:

    if (char.isalpha() and 'A' <= char <= 'Z') or (char.isdigit() and '0' <= char <= '5'):

        elements_set.add(char)


print("Множество элементов, встречающихся в последовательности:", elements_set)