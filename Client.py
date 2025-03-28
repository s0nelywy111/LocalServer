import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('26.10.173.114', 1111))
flag = True
while flag:
    request = input("Me: ")
    client.send(request.encode('utf-8'))
    if request == 'opera' or request == 'Opera' or request == 'req' or request == 'Req':
            search = client.send(input("Enter yout request: ").encode('utf-8'))
    

client.close()

