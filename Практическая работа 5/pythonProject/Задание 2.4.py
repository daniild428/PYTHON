n = 25
sum_of_numbers = 0
product_of_numbers = 1

print("Введите 25 чисел:")

for i in range(n):

  number = float(input(f"Введите число {i+1}: "))


  sum_of_numbers += number


  product_of_numbers *= number

print(f"Сумма чисел: {sum_of_numbers}")
print(f"Произведение чисел: {product_of_numbers}")