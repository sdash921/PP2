names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# Enumerate: Index and Value
print("Enumerate:")
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")

# Zip: Combine lists
print("\nZip:")
for name, score in zip(names, scores):
    print(f"{name} scored {score}")