def calculate_sum(n):
    sum_value = 0
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            sum_value += (n + i) / (2 * i + j + 1)
    return sum_value

n = int(input("Введите натуральное число n: "))
result = calculate_sum(n)
print("Значение суммы:", result)