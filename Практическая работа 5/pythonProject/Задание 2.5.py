n = 30
sum_of_squares = 0

for i in range(1, n + 1):

  even_number = 2 * i

  sum_of_squares += even_number ** 2

print(f"Сумма квадратов первых {n} четных чисел: {sum_of_squares}")