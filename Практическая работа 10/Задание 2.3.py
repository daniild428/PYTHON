
elements = set()


sequence = input("Введите последовательность символов: ")


for char in sequence:

    if char.isdigit() and '5' <= char <= '9':
        elements.add(char)
    elif char in ['+', '-', '*', '/']:
        elements.add(char)


print("Множество уникальных элементов:", elements)