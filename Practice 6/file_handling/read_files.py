def read_entire_file(filepath):
    with open(filepath, 'r') as f:
        print(f.read())

def read_line_by_line(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            print(line.strip())

if __name__ == "__main__":
    read_entire_file('../README.md')