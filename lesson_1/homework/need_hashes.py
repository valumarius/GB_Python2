import csv
import hashlib
import doctest


def hash_calc(string, algo_name):
    """
    Функция вычисления хэша строки по заданному алгоритму
    :param string: строка
    :param algo_name: название алгоритма
    :return: хэш строки
    >>> hash_calc("Python", "md5")
    'a7f5f35426b927411fc9231b56382173'
    """
    h = getattr(hashlib, algo_name)()
    h.update(bytes(string, encoding='utf-8'))
    return h.hexdigest()

if __name__ == '__main__':
    doctest.testmod()
    nested_list = []

    with open("need_hashes.csv", encoding='utf-8') as csvfile:
        csvtable = csv.reader(csvfile, delimiter=';')
        for row in csvtable:
            if len(row[2]) < 1:
                row[2] = hash_calc(row[0], row[1])
            nested_list.append(row)

    with open("need_hashes.csv", "w", encoding='utf-8', newline='') as newfile:
        hashwriter = csv.writer(newfile, delimiter=';')
        for row in nested_list:
            hashwriter.writerow(row)
