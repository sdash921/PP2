a = int(input())
gen = (x ** 2 for x in range(a) if x % 2 == 0 )
for i in gen:
    print(i)