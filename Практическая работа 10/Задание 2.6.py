sequence = input("Введите последовательность символов: ")
operation_set = set()

for char in sequence:
    if char in ['+', '-', '*', '/']:
        operation_set.add(char)

print("Множество арифметических операций:", operation_set)