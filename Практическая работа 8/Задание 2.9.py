string = input("Введите строку")
index_semicolon = string.find(';')

if index_semicolon != -1:
    characters_before_semicolon = index_semicolon
    print("Количество символов до точки с запятой:", characters_before_semicolon)
else:
    print("Точка с запятой не найдена в строке.")