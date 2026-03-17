from datetime import datetime
s = input()
a = int(input())
start = datetime.strptime(s,"%Y-%m-%d")

for _ in range(a):
    d = input()
    tech = datetime.strptime(d,"%Y-%m-%d")
    diff = (tech - start).days
    print(abs(diff))