import os
files = []
f = []
def get_addresses():
    directory = "files"

    files_and_dirs = os.listdir(directory)

    print("path:" + str(os.listdir(directory)))
    
    
    files = [f for f in files_and_dirs if os.path.isfile(os.path.join(directory, f))]
   
    for file in files:
        f.append(os.path.join(directory, file))
        print(os.path.join(directory, file))
        print(len(files))

    print(files)
    print(f)
    
get_addresses()