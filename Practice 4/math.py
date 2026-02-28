import math
import random

print(math.sqrt(16))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.pi)

options = ['Apple', 'Banana', 'Cherry']
print(random.choice(options))
print(random.randint(1, 100))

deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print(deck)