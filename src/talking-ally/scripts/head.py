#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# update: 2018/08/06 すべてのmoduleを統合 
# created by: tatsumi
#

# ros
import sys
import rospy

# okao module...
from okao.msg import *
from operator import itemgetter

# servo
import servo

# numpy
import numpy as np
import time

from shared import Shared


global addressX # face's direction x
global addressY # face's direction y


def arc_to_rad(arc):
    return arc * np.pi / 180.0


def init():
    global addressX
    global addressY
    addressX = addressY = 0.0
    servo.init()


def getPointFromOKAO(msg_okao):
    return getPointFromOKAOXY(msg_okao.x[0], msg_okao.y[0])


def getPointFromOKAOXY(okao_x, okao_y):
    if 0 < okao_x & okao_x < 1600:
        x = (800.0 - okao_x) / 800
    else:
        x = 0.0
    if 0 < okao_y & okao_y < 1200:
        y = (600.0 - okao_y) / 600
    else:
        y = 0.0
    return x, y


def nod():
    servo.move(1, 0.8)
    servo.move(2, 0.8)
    servo.move(3, -1.5)
    servo.move(4, 0)
    
    
def sit(rad=0.1):
    servo.move(1, rad)
    servo.move(2, rad)


"""
def addressing_arc(arcx, arcy):
    global addressX
    global addressY
    x = arc_to_rad(arcx)
    y = arc_to_rad(arcy)
    addressX = x
    addressY = y
    #print "rad: ", addressX, addressY
    servo.move(3, addressX)
    servo.move(4, addressY)
"""


def finding():
	print("finding!!")
	addressY = 0.0
	addressX = 0.0
	servo.move(3, addressY)
	servo.move(4, addressX)


def addressing(okao_x, okao_y):
    global addressX
    global addressY

    x, y = getPointFromOKAOXY(okao_x, okao_y)

    addressY = -2.2 * y
    addressX = x

    servo.move(3, addressY)
    servo.move(4, addressX)


def gazingRelatively_arc(arcx, arcy):
    x = arc_to_rad(arcx)
    y = arc_to_rad(arcy)
    #print "rad: ", x, y
    servo.move(1, x)
    servo.move(2, y)


def gazing(okao_x, okao_y):
    x, y = getPointFromOKAOXY(okao_x, okao_y)
    
    print(x, "--", y)
    #print "eye", x, y
    #print "face", addressX, addressY
    servo.move(1, x - addressX)
    servo.move(2, y - addressY)


def gazingRelatively(x, y):
    print(x, "--", y)
    a = np.array([0, 0])
    b = np.array([x, y])
    u = b - a
    d = np.linalg.norm(u)
    print 2 * d
    
    z = max(min(2 * d, 1.5), 0.1)
    servo.move(1, z * 1.5)
    servo.move(2, z)


def follow_eye(msg_okao):
    point = getPointFromOKAO(msg_okao)
    radx = point[0] * 0.5
    rady = point[1] * 0.5
    Shared.EYE_X = eye_x = radx - Shared.FACE_X
    Shared.EYE_Y = eye_y = rady + Shared.FACE_Y
    servo.move(1, eye_x)
    servo.move(2, -eye_y)
    return eye_x, eye_y


def follow_face_and_eye():
    eye_x = Shared.EYE_X
    eye_y = Shared.EYE_Y
    face_x = Shared.FACE_X
    face_y = Shared.FACE_Y
    tx = 0.03
    ty = 0.03
    if eye_x < 0:
        if eye_x > -tx:
            tx = -eye_x
        if face_x < tx - 1:
            tx = 1 + face_x
        eye_x = eye_x + tx
        face_x = face_x - tx
    else:
        if eye_x < tx:
            tx = eye_x
        if face_x > 1 - tx:
            tx = 1 - face_x
        eye_x = eye_x - tx
        face_x = face_x + tx
    servo.move(1, eye_x)
    servo.move(3, face_x)
    Shared.EYE_X = eye_x
    Shared.FACE_X = face_x

    if eye_y < 0:
        if eye_y > -ty:
            ty = -eye_y
        if face_y > 1 - ty:
            ty = 1 - face_y
        eye_y = eye_y + ty
        face_y = face_y + ty 
    else:
        if eye_y < ty:
            ty = eye_y
        if face_y < ty - 1:
            ty = 1 + face_y
        eye_y = eye_y - ty
        face_y = face_y - ty
    servo.move(2, eye_y)
    servo.move(4, face_y)
    Shared.EYE_Y = eye_y
    Shared.FACE_Y = face_y


def queue(src, a):
    dst = np.roll(src, -1)
    dst[-1] = a
    return dst


def getNearestValue(list, num):
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]


def jointAttention(okao):
    return 0

    jointAttentionEye(okao)
    jointAttentionFace(okao)


def jointAttentionEye(okao):
    return 0

    if okao.gazeLR[0] != 99999:
        Shared.gazeLR = queue(Shared.gazeLR, okao.gazeLR[0])
        Shared.gazeUD = queue(Shared.gazeUD, okao.gazeUD[0]-6)
    else:
        return None
    tx = 30.0
    ty = 20.0
    gazelr = max(min(np.average(Shared.gazeLR), tx), -tx)
    gazeud = max(min(np.average(Shared.gazeUD), ty), -ty)
    list1 = [-0.5, 0.0, 0.5]
    list2 = [0.0]
    lr = getNearestValue(list1, -gazelr / tx)
    ud = getNearestValue(list2, gazeud / ty)
    if lr != Shared.preGazeLR:
        servo.move(1, lr)
        Shared.preGazeLR = lr
    if ud != Shared.preGazeUD:
        servo.move(2, ud)
        Shared.preGazeUD = ud
    if lr != 0.0 or ud != 0.0:
        Shared.isLookingAwayEye = True
    else:
        Shared.isLookingAwayEye = False


def jointAttentionFace(okao):
    return 0

    if okao.LR[0] != 99999:
        Shared.LR = queue(Shared.LR, okao.LR[0])
        Shared.UD = queue(Shared.UD, okao.UD[0]-8)
    else:
        return None
    tx = 30.0
    ty = 20.0
    lr = max(min(np.average(Shared.LR), tx), -tx)
    ud = max(min(np.average(Shared.UD), ty), -ty)
    list3 = [-0.5, -0.25, 0.0, 0.25, 0.5]
    list4 = [-0.25, 0.0]
    lr = getNearestValue(list3, -lr / tx)
    ud = getNearestValue(list4, -ud / ty)
    if lr != Shared.preLR:
        servo.move(3, lr)
        Shared.preLR = lr
    if ud != Shared.preUD:
        print ud
        servo.move(4, ud)
        Shared.preUD = ud
    if lr == -0.5 or lr == 0.5 or ud != -0.25:
        Shared.isLookingAwayFace = True
    else:
        Shared.isLookingAwayFace = False


