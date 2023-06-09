#!/usr/bin/env python
# -*- coding: utf-8 -*-

import frida
import sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


with open('frida.js', 'r', encoding='utf8') as f:
    jscode = f.read()

device = frida.get_usb_device()
_process = device.get_process('猿人学2022')
process = device.attach(_process.pid)
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()