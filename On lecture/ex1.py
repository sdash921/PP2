def aka(a, b):
    c = False
    if a and b > 0:
        if a % b == 0:
            c = True
    return c
a = 10
b = 3
print(aka(a,b))