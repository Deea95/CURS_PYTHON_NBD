# read a file
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)

    except FileNotFoundError:
        print("File not found.")


read_file('path/file.txt')


# write file
def write_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

    print("Content written to file.")


write_file('path/file.txt', 'This is data.')