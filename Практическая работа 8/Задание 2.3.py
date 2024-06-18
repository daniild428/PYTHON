def count_rt(string):
    count_r = string.count('r')
    count_t = string.count('t')
    return count_r, count_t

input_string = input("Введите строку")
count_r, count_t = count_rt(input_string)
print(f"Количество символов 'r' в строке: {count_r}")
print(f"Количество символов 't' в строке: {count_t}")