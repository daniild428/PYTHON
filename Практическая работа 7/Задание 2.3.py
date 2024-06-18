n = int(input("Введите натуральное число n: "))

result = 0
for i in range(n + 1):
   for j in range(i + 1):
       result += (3 * i - j) / 2

print("Результат вычисления по формуле:", result)