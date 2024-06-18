input_string =input("Введите последовательость:")


result_set = set()


arithmetic_operators = set(['+', '-', '*', '/', '%'])
relational_operators = set(['>', '<', '==', '>=', '<=', '!='])


for char in input_string:

    if char in arithmetic_operators or char in relational_operators:
        result_set.add(char)


print(result_set)