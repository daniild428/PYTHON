a = float(input("Введите первое число a: "))
b = float(input("Введите второе число b: "))
c = float(input("Введите третье число c: "))

def square_or_power(num):
    if num >= 0:
        return num ** 2
    else:
        return num ** 4

result_a = square_or_power(a)
result_b = square_or_power(b)
result_c = square_or_power(c)

print(f"Результат для числа a: {result_a}")
print(f"Результат для числа b: {result_b}")
print(f"Результат для числа c: {result_c}")