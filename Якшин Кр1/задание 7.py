def count_syllables():
    M = int(input("Введите количество строк: "))
    strings = [input("Введите слово: ") for _ in range(M)]  
    syllable = input("Введите слог для подсчета: ")  
    
    for string in strings:
        print(f"{string}: {string.count(syllable)}")  

count_syllables()
