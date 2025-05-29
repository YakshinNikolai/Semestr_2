input_string = input("Введите строку: ")

result_string = ""
for index in range(len(input_string)):

    if index % 3 != 0:
        result_string += input_string[index]

print("Результат:", result_string)
