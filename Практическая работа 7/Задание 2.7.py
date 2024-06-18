def calculate_sum(n):
   result = 0
   for k in range(1, n+1):
       for m in range(k, n+1):
           result += (x + k) / m
   return result

# Пример использования
n = int(input("Введите натуральное число n: "))
x = int(input("Введите значение x: "))
result = calculate_sum(n)
print("Результат вычисления суммы:", result)