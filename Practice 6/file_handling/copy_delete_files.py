import shutil
import os

def copy_file(src, dest):
    shutil.copy2(src, dest)

def delete_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)

if __name__ == "__main__":
    copy_file('test.txt', 'test_copy.txt')
    delete_file('test_copy.txt')