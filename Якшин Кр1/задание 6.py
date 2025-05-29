def space_between_letters():
    M = int(input("Введите количество слов: "))
    
    for i in range(M):
        word = input(f"Введите слово {i + 1}: ")
        spaced_word = ' '.join(word)  
        print(f"Разрядка слова {i + 1}: {spaced_word}")

space_between_letters()
