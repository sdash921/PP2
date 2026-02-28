import re
line = input()
pattern = input()
a = re.findall(pattern, line)
b = 0
for i in a:
    b += 1
print (b)