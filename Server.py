import socket
import random
import pyautogui
import win32api,win32con
import time
import keyboard
import pyperclip
import subprocess

def IsClick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def IsCopy(name):
    pyperclip.copy(name)
    pyperclip.paste()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 1111))
server.listen()
client,address = server.accept()
flag= True
while flag:
    msg = client.recv(2048).decode('utf-8')
    if msg == 'exit':
        flag = False
    elif msg == 'Opera' or msg == 'opera':
        subprocess.Popen(["start", "opera"], shell=True)
        url = client.recv(2048).decode('utf-8')  # Получение URL от клиента
        keyboard.press('ctrl')
        keyboard.release('t')
        IsCopy(url)
        keyboard.press('ctrl')
        keyboard.send('v')
        keyboard.release('ctrl')
        keyboard.send('enter')
        print(url)
    else:
        print(msg)  # Вывод сообщения клиента
client.close()
server.close()
