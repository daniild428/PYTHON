import math

def calculate_y(t, a, b):
    if t == 0:
        return a + b
    elif t == 1:
        return math.sqrt(a**2 + b**2 * math.sin(1)) + b * math.cos(1)
    else:
        return calculate_y(t - 1, a, b) * math.sqrt(a**2 + b**2 * math.cos(1)) + b * math.sin(1)

a = 2.5
b = 0.4
t = int(input("Введите значение t: "))

if t >= 0:
    y = calculate_y(t, a, b)
    print(f"Значение y при t = {t} и a = {a}, b = {b}: {y}")
else:
    print("Значение t должно быть неотрицательным.")