from os.path import exists

def read_file(filename,user):
    try:
        if not exists(filename):
            raise FileNotFoundError(f"{filename} File Not Found")
        else:
            if user =='shyam':
                with open(filename) as f:
                    content = f.readlines()[:3]
                    print(content)
            else:
                raise PermissionError(f"User with name '{user}' does not have permission to read the file")

    except (FileNotFoundError, PermissionError) as e:
        print("Error : ",e)

    finally:
        print("File Operation Attempted")

filename=input("Enter File Name: ")
user = input("Enter User: ").lower()
read_file(filename,user)
