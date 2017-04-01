import random
import string


def create_file(file_name, folder, size):
    ascii_digit_string = (string.ascii_uppercase +
                          string.ascii_lowercase +
                          string.digits)
    if not size.isdigit():
        if size.endswith('KB'):
            int_size = int(size.split('KB')[0])
            size = int_size * 1024
        elif size.endswith('MB'):
            int_size = int(size.split('MB')[0])
            size = int_size * 1024 ** 2
        elif size.endswith('GB'):
            int_size = int(size.split('GB')[0])
            size = int_size * 1024 ** 3
        elif size.endswith('B'):
            size = int(size.split('B')[0])
    token = ''.join(random.choice(ascii_digit_string)
                    for _ in range(int(size)))
    with open(folder + file_name, "w") as file:
        file.write(token)


create_file("/test1.txt", "D:", '10KB')
create_file("/test2.txt", "D:", '1024')
create_file("/test11.txt", "D:", '2MB')
create_file("/test21.txt", "D:", '1B')
