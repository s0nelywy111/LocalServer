import socket

client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect(('192.168.137.57', 1111))

flag = True
while flag:
    client1.send(input("Me: ").encode('utf-8'))
    msg = client1.recv(2048).decode('utf-8')
    if msg == 'exit':
        flag = False
    else:
        print(msg)
client1.close()

