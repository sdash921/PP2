n = int(input())
m = list(map(int,input().split()))
m = m[:n]
avg = 0
for i in range(0,n):
    avg += m[i]
avg = avg/n
c = 0
for i in range(0,n):
    if m[i] > avg:
        c += 1

print(c)