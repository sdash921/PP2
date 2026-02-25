def is_even(n):
    if(n % 2 == 0): #simple check when n number divides by 2 to check if it has left any remainders. 
        print('even') #if no then it is even
    else:
        print("Not even")
a = int(input())
is_even(a)