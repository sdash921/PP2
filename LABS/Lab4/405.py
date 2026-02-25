def numbers_go_down(x):
    for i in range(x, -1, -1):
        yield i
x = int(input())
for i in numbers_go_down(x):
    print(i)