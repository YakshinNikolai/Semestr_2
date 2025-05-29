s = input()
n = len(s)
mid = (n + 1) // 2
result = s[mid:] + s[:mid]
print(result)
