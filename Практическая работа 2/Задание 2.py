import math

# Ввод значений x и y
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

# Вычисление выражения
b = abs(math.pow(y, x) - math.sqrt(3) * math.sqrt(x))

# Вывод результатов
print("x =", x)
print("y =", y)
print("b =", b)

# Вывод целой части результата
print("Целая часть b =", int(b))
