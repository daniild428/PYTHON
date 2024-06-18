import math

x = float(input("Введите значение x: "))
b = float(input("Введите значение b: "))

if b < 1:
    y = b * x - math.log(b * x)
elif b == 1:
    y = b * x
else:
    y = b * x + math.log(b * x)

print("Значение y:", y)