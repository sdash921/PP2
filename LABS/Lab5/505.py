import re
a = input()
pattern = re.compile("^[A-Z]|^[a-z]+[0-9]+$")
b = bool(pattern.search(a))
if b:
    print('Yes')
else:
    print("No")
#example: Hello123, World456, Python789
#output: Yes, Yes, Yes