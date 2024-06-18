x = float(input("Введите число x: "))
y = float(input("Введите число y: "))

if x < y:
    x_new = 0.5 * (x + y)
    y_new = 2 * x * y
else:
    x_new = 2 * x * y
    y_new = 0.5 * (x + y)

print(f"Результат: x = {x_new}, y = {y_new}")