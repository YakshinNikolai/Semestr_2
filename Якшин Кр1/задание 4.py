def main():
    odd_sum = 0
    even_product = 1
    odd_count = 0
    even_count = 0
    index = 1

    while True:
        number = int(input("Введите число (или 55555 для завершения): "))
        
        if number == 55555:
            break
        
        if index % 2 == 1:  
            odd_sum += number
            odd_count += 1
        else:  
            even_product *= number
            even_count += 1
        
        index += 1

    print(f"Сумма нечётных: {odd_sum}, Произведение чётных: {even_product if even_count > 0 else 0}")
    print(f"Количество нечётных: {odd_count}, Количество чётных: {even_count}")

if __name__ == "__main__":
    main()