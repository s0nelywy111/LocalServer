import socket
import random
import pyautogui
import win32api,win32con
import time
import keyboard
import pyperclip

def IsClick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def IsCopy(name):
    pyperclip.copy(name)
    pyperclip.paste()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.137.57', 1111))
server.listen()
client,address = server.accept()
flag= True
while flag:
    msg = client.recv(2048).decode('utf-8')
    if msg == 'exit':
        flag = False
    elif msg == 'Opera'or msg == 'opera':
        IsClick(162,1048)
        msg = client.recv(2048).decode('utf-8')
        keyboard.press('ctrl')
        keyboard.release('t')
        keyboard.release('ctrl')
        IsCopy(msg)
        keyboard.press('ctrl')
        keyboard.send('v')
        keyboard.release('ctrl')
        keyboard.send('enter')
    else:
        msg = client.recv(2048).decode('utf-8')
client.close()
server.close()
