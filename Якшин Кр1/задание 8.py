input_string = input("Введите строку: ")

if len(input_string) >= 3:
    print(input_string[2])  
else:
    print("Строка слишком короткая.")

if len(input_string) >= 2:
    print(input_string[-2])  
else:
    print("Строка слишком короткая.")

print(input_string[:5])  

print(input_string[:-2])  

print(input_string[::2])  

print(input_string[1::2])  

print(input_string[::-1])  

print(input_string[::-2])  

print(len(input_string))  
