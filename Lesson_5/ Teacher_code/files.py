def work_with_files_append(path_to_file: str = 'test_file.txt', data=''):
    with open(path_to_file, 'a') as file:
        file.write(data)


def work_with_files_read(path_to_file: str = 'test_file.txt'):
    with open(path_to_file, 'r') as file:
        # print(file.read())
        print(file.readline())
        # print(file.readlines())


# unicode
unic = '\U0001F3D6'
print(unic)
