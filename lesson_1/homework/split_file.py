import hashlib
import string
from random import sample


def split_file(file, splitsize=1024):
    """
    Функция разбиения файла на части
    :param file: имя файла для разбиения
    :param splitsize: размер части 
    :return: количество частей
    """
    with open(file, 'r+b') as src:
        chars = string.ascii_letters + string.digits
        length = 8
        counter = 0
        while True:
            with open('parts.md5', 'a') as md5file:
                    written = 0
                    while written < splitsize:
                        data = src.read(splitsize)
                        if data:
                            filename = ''.join(sample(chars, length))
                            with open(filename, 'w+b') as tgt:
                                tgt.write(data)
                            h = hashlib.md5()
                            h.update(data)
                            md5file.write(h.hexdigest() + '\n')
                            written += splitsize
                        else:
                            return counter
                    counter += 1
