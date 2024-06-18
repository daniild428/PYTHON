def remove_duplicates_and_spaces(input_string):
    result = ""
    for char in input_string:
        if char.isalpha() and char not in result:
            result += char
    return result

input_string = input("Введите строку: ")
output_string = remove_duplicates_and_spaces(input_string.replace(" ", ""))

print("Результат после удаления дублирующих символов и пробелов:", output_string)