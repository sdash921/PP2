def even_with_comma(x):
    y = 0
    while y <= x:
        yield y 
        y = y + 2

x = int(input())
for i in even_with_comma(x):
    if i == x or i == x - 1:
        print(i)
    else:
        print(i, end = ",")