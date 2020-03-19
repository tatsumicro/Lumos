#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

from wizavo.srv import *
import rospy

# wizavo module
import wizavo_socket

# subprocess
import subprocess
import threading
import time

portfile = "/home/icd/catkin_ws/src/wizavo/scripts/port.txt"

def handle_add_two_ints(req):
    wavfile = wizavo_socket.create(req.req)
    return wizavoResponse(wavfile)


def server_init():
    rospy.init_node('wizavo_server')
    s = rospy.Service('wizavo_topic', wizavo, handle_add_two_ints)
    print "Ready to echo string."
    rospy.spin()

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
    server_init()


