def shortener(st):
    result = []
    stack = []
    skip = False  

    for char in st:
        if char == '(':
            stack.append(char)  
            skip = True  
        elif char == ')':
            if stack:
                stack.pop()  
                if not stack:  
                    skip = False
        else:
            if not skip:
                result.append(char)  

    return ''.join(result)


print(shortener("Основы проектной деятельности (в колледже) будет на первом курсе"))  
print(shortener("А также (Обществознание (История) Литература)"))  
print(shortener("Вы дложны были назначить дежурных"))  
print(shortener("(Петров) Иванов"))  
