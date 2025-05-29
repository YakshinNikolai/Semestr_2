s = input("Введите строку: ")

result = ''

for char in s:
    if char != ' ' and char not in result:
        result += char
        
print(f"Результат: '{result}'")
