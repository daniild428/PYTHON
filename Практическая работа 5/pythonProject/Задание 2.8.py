a = 5
d = 4
target_sum = 324
n = 0
current_sum = 0
while current_sum < target_sum:
    n += 1
    current_sum += a + (n - 1) * d

print(f"Необходимо взять {n} слагаемых, чтобы получить сумму 324.")