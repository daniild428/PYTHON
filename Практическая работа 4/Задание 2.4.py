import math

a = 2.5

x = float(input("Введите значение x: "))

if x > a:
    y = (x**3/3) - a
elif x == a:
    y = x * math.sin(a*x)
else:
    y = math.exp(-a*x) * math.cos(a*x)

print("Значение y:", y)