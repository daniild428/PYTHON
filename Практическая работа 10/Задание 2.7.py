input_string = ".Phyton"


result_set = set()


for char in input_string:

    if char.isalpha() and 'E' <= char.upper() <= 'N':
        result_set.add(char.upper())
    elif char in ['.', ',', '!', '?', ':', ';']:
        result_set.add(char)


print(result_set)