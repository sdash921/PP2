# Writing (w)
with open("test.txt", "w") as f:
    f.write("Hello World\n")

# Appending (a)
with open("test.txt", "a") as f:
    f.writelines(["Line 2\n", "Line 3\n"])

# Reading (r)
with open("test.txt", "r") as f:
    content = f.read() # Entire file as string
    # OR: lines = f.readlines() # File as a list of strings