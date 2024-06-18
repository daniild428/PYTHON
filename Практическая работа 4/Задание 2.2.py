import math

# Ввод исходных данных
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))

# Ввод значения x
x = float(input("Введите значение x: "))

# Вычисление значения функции y
if x <= 1.2:
    y = (a * x + math.sqrt(x**2 + 1)) / (a + b * math.sqrt(x**2 + 1))
else:
    y = (a * x + math.sqrt(x**2 + 1)) / (a + b * math.sqrt(x**2 + 1))

# Вывод значения функции y
print("Значение функции y:", y)