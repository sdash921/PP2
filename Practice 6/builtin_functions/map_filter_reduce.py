from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# Map: Square all numbers
squared = list(map(lambda x: x**2, nums))

# Filter: Only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))

# Reduce: Sum of all numbers
total = reduce(lambda x, y: x + y, nums)

print(f"Original: {nums}")
print(f"Squared: {squared}")
print(f"Evens: {evens}")
print(f"Total: {total}")