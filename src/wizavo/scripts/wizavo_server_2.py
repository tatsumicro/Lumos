#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

# wizavo module
import wizavo_socket

# subprocess
import subprocess
import threading
import time

portfile = "/home/icd/wizavo/scripts/port.txt"


def reset_port():
    port = int(open(portfile).read())
    newport = port + 1
    if newport > 65535:
        newport = 49152
    with open(portfile, mode='w') as f:
        f.write(str(newport))
    print(newport)


def wizavo_socket_init():
    reset_port()
    addr = 'localhost'
    port = int(open(portfile).read())
    wizavo_socket.init(addr, port)
    print("############################connection is completed!")


if __name__ == "__main__":
    wizavo_socket_init()
    
    while True:
        string = raw_input('input: ')
        string = unicode(string, 'utf-8')
        print(string)
        
        wavfile = wizavo_socket.create(string)
        print(wavfile)




