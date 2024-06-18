m = int(input("Введите число m: "))
n = int(input("Введите число n: "))

if m != n:
    new_number = max(m, n)
else:
    m = n = 0

print(f"Результат: m = {m}, n = {n}")