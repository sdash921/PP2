def write_new_file(filepath, content):
    with open(filepath, 'w') as f:
        f.write(content)

def append_to_file(filepath, content):
    with open(filepath, 'a') as f:
        f.write(f"\n{content}")

if __name__ == "__main__":
    write_new_file('test.txt', 'Hello Python!')
    append_to_file('test.txt', 'Appending new line.')