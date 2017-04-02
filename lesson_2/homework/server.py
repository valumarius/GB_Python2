
# Сервер игры "Запоминалка"

import socketserver
from datetime import datetime
import random





class MemTCPHandler(socketserver.BaseRequestHandler):

    def intdate_to_datetime(self, intdate, intseconds):
        self.year = intdate // 512 + 2000
        self.month = (intdate % 512) // 32
        self.day = (intdate % 512) % 32
        self.hours = intseconds // 3600
        self.minutes = (intseconds % 3600) // 60
        self.seconds = (intseconds % 3600) % 60
        return datetime(self.year, self.month, self.day,
                        self.hours, self.minutes, self.seconds)

    def handle(self):
        self.data = self.request.recv(1024)
        self.header = str(self.data[:2], 'ascii')
        self.intdate = int.from_bytes(self.data[2:4], 'big')
        self.intseconds = int.from_bytes(self.data[4:7], 'big')
        self.datetime = self.intdate_to_datetime(self.intdate,
                                                 self.intseconds)
        self.transact_type = self.data[7]
        print("Клиент {} сообщает {} {} {}".format(self.client_address[0],
                                                   self.header,
                                                   self.datetime,
                                                   self.transact_type))

        if self.header == 'zz':
            print("Transaction")
            if self.transact_type == 0:
                print("Сервисная транзакция")
            elif self.transact_type == 1:
                print("Платежная транзакция")
            elif self.transact_type == 2:
                print("Инкассация")
            else:
                print('Неизвестный запрос')
            self.request.sendall(b'ok')
        else:
            print('Неизвестный запрос')    

          
HOST, PORT = 'localhost', 9999

server = socketserver.TCPServer((HOST, PORT), MemTCPHandler)  
print('Сервер препроцессинга запущен')

server.serve_forever()

