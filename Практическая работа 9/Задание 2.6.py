def replace_substring(s, old_substring, new_substring):
    if old_substring in s:
        s = s.replace(old_substring, new_substring)
        print("Новая строка после замены:", s)
    else:
        print("Подстрока для замены не найдена в строке.")

# Ввод строк пользователем
string = input("Введите строку: ")
old_substring = input("Введите подстроку для замены: ")
new_substring = input("Введите новую подстроку: ")

# Вызов функции для замены подстроки
replace_substring(string, old_substring, new_substring)

