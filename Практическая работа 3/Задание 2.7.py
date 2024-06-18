a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

count = 0

if 10 <= a < 100:
    count += 1
if 10 <= b < 100:
    count += 1
if 10 <= c < 100:
    count += 1

print(f"Количество двузначных чисел: {count}")