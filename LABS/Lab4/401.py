def square(x):
    y = 1
    z = y ** 2
    while y <= x:
        yield z
        y = y + 1 
        z = y ** 2
x = int(input())
for i in square(x):
    print(i)
    
    