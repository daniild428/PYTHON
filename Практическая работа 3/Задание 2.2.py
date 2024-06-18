a = float(input("Введите первое число a: "))
b = float(input("Введите второе число b: "))

if abs(a) > abs(b):
    a /= 5

print(f"Результат: a = {a}, b = {b}")
