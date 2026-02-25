x = int(input())
y = iter(range(0, x + 1))
for i in y:
    if i % 3 == 0 and i % 4 == 0:
        print(i, end=" ")