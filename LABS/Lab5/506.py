import re
a = input()
pattern = re.compile(r"\S+@\S+\.\S+") # pattern for email-like strings
b = bool(pattern.search(a))
if b:
    print(pattern.search(a).group()) # print the matched email-like substring
else:
    print("No email")