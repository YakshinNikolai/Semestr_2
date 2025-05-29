s = input()

first_index = s.find('h')
last_index = s.rfind('h')

result = s[:first_index] + s[last_index + 1:]

print(result)
