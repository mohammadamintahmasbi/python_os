import hashlib


def hash_to_md5(filenames: [str]):
    for filename in filenames:
        with open(filename, 'r') as file:
            content = file.read()
            result = hashlib.md5(str(content).encode()).hexdigest()
            print(result)
        md5_file_name = ".".join(filename.split(".")) + ".md5"
        with open(md5_file_name, 'w') as file:
            file.write(str(result))