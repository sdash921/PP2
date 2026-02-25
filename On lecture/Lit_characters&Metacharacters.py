import re
store = re.compile(r"^(Book|Mattress|Grocery)store$")
supplier = re.compile(r"^(Book|Mattress|Grocery)supplier$")
s = input()
print(s + ":", bool(store.search(s))

