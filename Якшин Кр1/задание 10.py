s = input()

first_index = s.find('f')
last_index = s.rfind('f')

if first_index != -1:
    if first_index == last_index:
        print(first_index)
    else:
        print(first_index, last_index)
