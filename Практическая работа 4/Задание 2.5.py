import math

# Ввод данных
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))

# Проверка условия для y1
x = float(input("Введите значение x: "))  # Объявление переменной x
if 2.28 <= a * x <= 6:
    y1 = math.exp(a * x + math.cos(x)) / (a * (a + b) * (x + 1))
    print("y1 =", y1)

# Проверка условия для y2
if 6 <= x <= 8:
    y2 = math.exp(a * x + math.sin(x))
    print("y2 =", y2)