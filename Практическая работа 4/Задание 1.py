def check_sign(number):
    if number > 0:
        print("+")
    elif number < 0:
        print("-")
    else:
        print("0")

# Считываем число с клавиатуры
try:
    num = float(input("Введите дробное число: "))
    check_sign(num)
except ValueError:
    print("Ошибка: Введите дробное число.")
