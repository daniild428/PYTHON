import math

x = float(input("Введите значение x: "))

if x < 0:
    t = 2.2
    y = (math.log(abs(x**2 + y)) * math.sqrt(abs(x + t)))
elif x == 0.5:
    y = (math.sqrt(abs(x + t + 1)) / x)
else:
    y = (math.cos(x) + math.sin(x**2))

print("y =", y)