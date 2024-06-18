import math

# Ввод значения x
x = float(input("Введите значение x: "))

# Проверка условия x > 1, x = 1, x < 1
if x > 1:
    a = 1.65
    y = (math.pi**2 - 7) / x**2
    ln_x = math.log(x + 7) / math.sqrt(x + a)
    print("y = ", y)
    print("ln(x) = ", ln_x)
elif x == 1:
    a = 1.65
    y = (math.pi**2 - 7) / x**2
    ln_x = math.log(x + 7) / math.sqrt(x + a)
    print("y = ", y)
    print("ln(x) = ", ln_x)
else:
    a = 1.65
    y = (math.pi**2 - 7) / x**2
    ln_x = math.log(x + 7) / math.sqrt(x + a)
    print("y = ", y)
    print("ln(x) = ", ln_x)