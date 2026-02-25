#today is func with yield and the numbers that are prime
def prime_numbers(n):
    for num in range(2, n + 1):
        is_prime = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield num
n = int(input())
for prime in prime_numbers(n):
    print(prime, end=' ')