import re
line = input()
pattern = input()
a = bool(re.compile(pattern).search(line))
if a:
    print("Yes")
else:
    print("No")