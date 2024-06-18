def insert_commas(text):
    return ', '.join(text.split())


input_text = input("Введите строку ")
output_text = insert_commas(input_text)
print(output_text)