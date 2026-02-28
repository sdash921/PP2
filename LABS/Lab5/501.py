import re
pattern = input()
a = bool(re.compile("^Hello").search(pattern))
if a:
    print("Yes")
else:
    print("No")
