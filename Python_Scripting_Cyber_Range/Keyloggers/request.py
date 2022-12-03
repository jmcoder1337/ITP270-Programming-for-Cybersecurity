#!#!/usr/bin/env python3

import requests

url='https://docs.google.com/forms/u/0/d/e/1FAIpQLSdLzNq4ZFtEfEd_mbhcX-YxNH5k7_a6NYgxEjEw2jkhCxXJaQ/formResponse'

form_data = {'entry.839337160': 'This is a test also (From Kali Linux Server)'}

r = requests.post(url, data=form_data)
