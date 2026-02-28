import re
a = input()
numbers = re.compile("[0-9]")

yeah = re.findall(numbers,a)

for i in yeah:
    print(i,end=" ")