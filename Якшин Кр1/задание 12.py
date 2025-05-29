s = input()

first_index = s.find('h')
last_index = s.rfind('h')

substring = s[first_index + 1:last_index]

result = substring * 2
print(result)
