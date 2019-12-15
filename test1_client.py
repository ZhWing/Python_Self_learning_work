# home/cube/Python自主学习
# _*_ coding: UTF-8 _*_
# 文件名:client.py

import socket

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 12345
s.connect((host, port))
s.send("我是客户端,现在申请连接".encode("utf-8"))
print(s.recv(1024).decode("utf-8"))
s.close()
