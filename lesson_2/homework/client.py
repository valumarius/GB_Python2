import socket
from datetime import datetime, time

HOST, PORT = 'localhost', 9999


def date_encode(now):
    """
    Функция кодирования даты (год, месяц, число) в 2 байта
    :return: 
    """
    date = 512 * (now.year - 2000) + 32 * now.month + now.day
    return date.to_bytes(2, 'big')


def seconds_from_midnight(now):
    """
    Функция кодирования секунд начиная от полуночи в 3 байта
    :return: 
    """
    midnight = datetime.combine(now.date(), time(0))
    delta = now - midnight
    return delta.seconds.to_bytes(3, 'big')

print('Клиент запущен')

# now = datetime.now()
transact_type = 8
while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    print('Введите тип транзакции: \n'
          '0 - сервисная \n'
          '1 - платежная \n'
          '2 - инкассация\n'
          '9 - выход')
    try:
        transact_type = int(input())
    except ValueError:
        print('Неверный ввод')
    if transact_type == 9:
        sock.sendall(b'qq')
        break
    elif transact_type != 8:
        try:
            ttype_bin = transact_type.to_bytes(1, 'big')
            packet = b'zz' + date_encode(datetime.now()) + \
                     seconds_from_midnight(datetime.now()) + ttype_bin
            sock.sendall(packet)
            recvd = str(sock.recv(1024), 'ascii')
            print(recvd)
        except OverflowError:
            print('Неверный ввод')

sock.close()

