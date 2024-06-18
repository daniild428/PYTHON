input_string = input("Введите последовательнорсть:")


result_set = set()


for char in input_string:

    if char in 'ABCDEFXYZ':
        result_set.add(char)


print(result_set)