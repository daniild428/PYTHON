a = 3
total_sum = 0


for num in range(1000, 10000):

  if num % a == 0:
    total_sum += num


print("Сумма всех 4-значных чисел, кратных", a, "равна", total_sum)