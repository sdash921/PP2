my_list = ["Python", "Java", "C++"]
it = iter(my_list)
print(next(it))
print(next(it))

def fibonacci_gen(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci_gen(5):
    print(num)

squares = (x**2 for x in range(5))
print(list(squares))