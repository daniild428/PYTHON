sequence = input("Введите последовательность цифр от '0' до '9': ")
unique_digits = set()

# Перебираем символы в последовательности и добавляем уникальные цифры в множество
for char in sequence:
    if char.isdigit():
        unique_digits.add(char)

# Вывод уникальных цифр
print("Множество уникальных цифр из введенной последовательности:")
print(unique_digits)