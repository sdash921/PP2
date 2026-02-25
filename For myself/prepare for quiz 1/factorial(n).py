def factorial(n):
    b = 1
    for i in range(1,n + 1):
        b = b * i
    return b
a = int(input())
print(factorial(a))