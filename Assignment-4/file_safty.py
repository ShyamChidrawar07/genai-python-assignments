import os

def read_file(filename: str) -> None:
    if os.path.exists(filename):
        with open(filename, "r") as f:
            print(f.read())
    else:
        print("File not found. Please check the filename.")

filename = input("Enter filename: ")
read_file(filename)
