def square_from_two_range(x, a):
    z = x ** 2
    for i in range(x, a + 1):
        yield z
        x = x + 1 
        z = x ** 2
x = list(map(int, input().split()))
a = x[1]
x = x[0]
for i in square_from_two_range(x, a):
    print(i)
    