import os

def path_info(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print("Path exists.")
        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("Path does not exist.")

