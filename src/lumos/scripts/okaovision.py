#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# created by: tatsumi
#

import rospy
from okao.msg import *
import numpy as np


global PEOPLE
global BUF

def init():
    print("initialize!!")
    global BUF
    BUF = 0
    global people
    people = {}
    rospy.Subscriber('lumos/chatter_okao', face_info, callback)


def callback(msg):
    print("okao:: ", msg.face_count)
    global BUF
    global people
    people = {}
    for idx in range(msg.face_count):
        people[msg.id[idx]] = getHuman(msg, idx)
    
    BUF = msg.UD[0]

    """
    if msg.face_count > 0:
        BUF= int(msg.UD[0])
    else:
        BUF = int(0)
    if msg.face_count > 0:
        BUF = msg.UD[0]
    else:
        pass
    """
    

def get():
    return int(BUF)


def getHuman(msg, idx):
    human = {"id":msg.id[idx],\
             "x":msg.x[idx],\
             "y":msg.y[idx],\
             "size":msg.size[idx],\
             "LR":msg.LR[idx],\
             "UD":msg.UD[idx],\
             "gazeLR":msg.gazeLR[idx],\
             "gazeUD":msg.gazeUD[idx]}
    return human

