# user/bin/python
# _*_ coding: UTF-8 _*_
# 文件名:socker_1.py

import socket

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print('地址:', addr, "申请链接")
    d = c.recv(1024)
    d = d.decode("utf-8")
    print("客户端发来消息:", d)
    cReturn = '欢迎访问[来自:Server( ' + host + ')]'
    c.send(cReturn.encode("utf-8"))
    c.close()
