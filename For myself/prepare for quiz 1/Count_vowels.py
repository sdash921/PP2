def count_vowels(a):
    h = ['a','e','o','y','u','i']
    b = 0
    for i in range(0, len(a)):
        if a[i] in h:
            b += 1
    return b
a = str(input())
print(count_vowels(a))