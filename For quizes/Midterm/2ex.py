import json
import re

s = json.loads(input())
for name, email in s.items():
    if "@" in email and "." in email:
        print(name)
        