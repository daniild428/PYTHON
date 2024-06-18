import math

t = float(input("Введите значение t: "))

if 1 <= t <= 2:
    a = -0.5
    b = 2
    y = 1 - math.e ** (a * math.cos(b * t))
else:
    y = None

print("y =", y)
