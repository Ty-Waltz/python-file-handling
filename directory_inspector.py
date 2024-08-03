import os

def list_directory_contents(path):
    try:
        if not os.path.isdir(path):
            print(f"Error:'{path}' is not a valid directory.")
            return
        print(f"Contents of directory '{path}':")
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(f"Directory: {item}")
            else:
                print(f"File: {item}")
    
    except PermissionError:
        print(f"Error: permission error occured '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    directory = input("Enter the directory path to list: ").strip()
    list_directory_contents(directory)