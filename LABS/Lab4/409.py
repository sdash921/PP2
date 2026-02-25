def the_pow_of_2_by_yield(n):
    for i in range(n + 1):
        yield 2 ** i
n = int(input())
for power in the_pow_of_2_by_yield(n):
    print(power, end=' ')