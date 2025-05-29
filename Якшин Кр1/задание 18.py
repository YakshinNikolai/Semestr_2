original_string = input("Введите строку: ")

substring_to_replace = input("Введите заменяемую подстроку: ")
new_substring = input("Введите новую подстроку: ")
result_string = original_string.replace(substring_to_replace, new_substring)

print(f"Результат: '{result_string}'")
