#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

from srv_test.srv import *
import rospy

# wizavo module
import wizavo

# subprocess
import subprocess
import threading
import time


def handle_add_two_ints(req):
    wavfile = wizavo.create(req.req)
    return testResponse(wavfile)


def server():
    rospy.init_node('test_topic_server')
    s = rospy.Service('test_topic', test, handle_add_two_ints)
    print "Ready to echo string."
    rospy.spin()


def reset_port():
    port_dir = '/home/icd/catkin_ws/src/srv_test/scripts/port.txt'
    port = int(open(port_dir).read())
    newport = port + 1
    if newport > 65535:
        newport = 49152
    with open(port_dir, mode='w') as f:
        f.write(str(newport))
    print(newport)


def wizavo_init():
    reset_port()
    addr = 'localhost'
    port = int(open('/home/icd/catkin_ws/src/srv_test/scripts/port.txt').read())
    wizavo.init(addr, port)
    print("############################connection is completed!")


if __name__ == "__main__":
    wizavo_init()
    server()

