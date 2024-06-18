text = 'В строке удалить символ ( : ) и подсчитать количество удаленных\nсимволов. код на \nPython'
modified_text = text.replace(':', '')
removed_count = len(text) - len(modified_text)
print("Количество удаленных символов равно:", removed_count)