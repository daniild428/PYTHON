def remove_spaces(s):
    return s.replace(" ", "")

def is_palindrome(s):
    s = remove_spaces(s)
    return s == s[::-1]

# Считываем строку от пользователя
user_input = input("Введите строку: ")

if is_palindrome(user_input):
    print("Данная строка является палиндромом.")
else:
    print("Данная строка не является палиндромом.")