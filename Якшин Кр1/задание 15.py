s = input("Введите строку: ")

count_lower = 0
count_upper = 0

for char in s:
    if char.islower(): 
        count_lower += 1
    elif char.isupper():  
        count_upper += 1

print(f"Количество строчных букв: {count_lower}")
print(f"Количество прописных букв: {count_upper}")
