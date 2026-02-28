import re
a = input()
pattern = input()
replacement = input()
result = re.sub(pattern, replacement, a)
print(result)