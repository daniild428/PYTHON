n = 40
sum_of_squares = 0

for i in range(n):

  odd_number = 2 * i + 1

  sum_of_squares += odd_number ** 2

print(f"Сумма квадратов первых {n} нечетных чисел: {sum_of_squares}")