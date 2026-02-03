def is_palindrom(a):
    if(a == a[::-1]):
        print('Yeh it is palindrome')
    else:
        print('Nah it is not a palindrome')
a = input()
is_palindrom(a)
