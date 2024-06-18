text = input("Введите строку")
semicolon_index = text.find(";")

if semicolon_index != -1:
    count = len(text) - semicolon_index - 1
    print(f"Количество символов после точки с запятой: {count}")
else:
    print("В строке нет точки с запятой.")