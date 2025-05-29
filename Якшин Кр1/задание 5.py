def count_spaces_in_lines():
    M = int(input("Введите количество строк: "))

    for i in range(M):
        line = input(f"Введите строку {i + 1}: ")
        count = line.count(' ')  
        print(f"Количество пробелов в строке {i + 1}: {count}")

count_spaces_in_lines()
