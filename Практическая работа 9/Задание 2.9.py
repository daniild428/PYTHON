import re

def check_identifier(word):
    pattern = r'^[a-zA-Z_]\w*$'
    if re.match(pattern, word):
        return True
    else:
        return False

word = input("Введите слово: ")
if check_identifier(word):
    print("Слово является идентификатором")
else:
    print("Слово не является идентификатором")