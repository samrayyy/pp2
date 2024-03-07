import os

def delete_file(path):
    if not os.path.exists(path):
        print("File does not exist")
        return

    if not os.access(path, os.F_OK):
        print("No access to the file")
        return

    try:
        os.remove(path)
    except Exception as e:
        print("Error")
