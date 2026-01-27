r = range(1, 6)
print("Numbers in range:", list(r))
for i in r:
    print(i * 2)
print(type(r))# range ya
# range is taking from 1 to 5, and it is not taking 6 because thats how it works. Takes (first number + second num... last num - 1)
# but we also can modify range
r = range(5, 0, -1)  # start at 5 stop before 0 but it minus 1 every step
print("Numbers in reverse range:", list(r))
for i in r:
    print(i * 2)
print(type(r))
