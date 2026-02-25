def cycle_list(lst, n):
    for _ in range(n):
        for item in lst:
            yield item
x = list(input().split())
y = int(input())
for element in cycle_list(x, y):
    print(element, end=' ')