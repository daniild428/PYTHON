def sum_formula(n):
   sum1 = (n + 1) * (n + 1) * (2 * n + 1) // 6
   sum2 = n * (n + 1) // 2
   return (n + 1) * (sum1 - sum2)

n = int(input("Введите натуральное число n: "))
result = sum_formula(n)
print("Результат:", result)