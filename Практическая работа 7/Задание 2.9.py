def calculate_sum(n):
    sum_result = 0
    for k in range(1, n+1):
        for m in range(1, n+1):
            sum_result += n / (2*k + m)
    return sum_result

n = int(input("Введите натуральное число n: "))
result = calculate_sum(n)
print("Результат вычисления по формуле:", result)