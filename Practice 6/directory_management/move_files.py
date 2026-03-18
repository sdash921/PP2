import shutil
import os

def move_file(src, dest_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    shutil.move(src, os.path.join(dest_folder, os.path.basename(src)))

if __name__ == "__main__":
    # Assumes test.txt exists from previous script
    move_file('test.txt', 'temp_dir')