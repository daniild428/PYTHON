input_string = input("Введите последовательность:")


result_set = set()


digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
arithmetic_operators = set(['+', '-', '*', '/', '%'])


for char in input_string:

    if char in digits or char in arithmetic_operators:
        result_set.add(char)


print(result_set)