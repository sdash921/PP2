def even_numbers(a):
    for i in range(0, a):
        if i % 2 == 0:
            yield i ** 2

a = int(input("Enter limit: "))
gen = even_numbers(a)

for value in gen:
    print(value)

