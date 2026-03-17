import re
s = str("Error code: 404, User: admin_12, Status: Failed")
pattern = r'\d{3}'
match = re.search(pattern,s)
if match:
    print(match)