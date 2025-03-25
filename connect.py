import socket

client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect(('192.168.137.57', 1111))

flag = True
while flag:
    client1.send(input("Me: ").encode('utf-8'))
client1.close()

