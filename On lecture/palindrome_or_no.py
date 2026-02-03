def is_palindrom(a):
    if(a == a[::-1]):
        print('Yes, it is a palindrome')
    else:
        print('No, it is not a palindrome')
a = input()
is_palindrom(a)
