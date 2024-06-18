def symbols_before_colon(s):
    index = s.find(':')
    if index != -1:
        return index
    else:
        return 0

# Пример использования функции
string = input("Введите строку")
result = symbols_before_colon(string)
print(result)  