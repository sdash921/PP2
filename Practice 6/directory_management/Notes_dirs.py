import os

def manage_dirs():
    dir_name = "temp_dir"
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    
    print(f"Contents of current directory: {os.listdir('.')}")

if __name__ == "__main__":
    manage_dirs()