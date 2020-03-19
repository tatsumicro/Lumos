#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# created by: M.Tatsumi
# update:     2019/08/25
#

import rospy
from my_dynamixel_tutorial.msg import *


global RAD_PUB
global SPE_PUB


def init():
    global RAD_PUB
    global SPE_PUB
    RAD_PUB = rospy.Publisher('servo_info', servo_rad, queue_size=1)
    SPE_PUB = rospy.Publisher('servo_set_speed', servo_speed, queue_size=1)


def move(servo_id, rad):
    move(servo_id, rad, 1.0)


def move(servo_id, rad, spd):
    r = rospy.Rate(1000)
    msg_rad = servo_rad()
    msg_rad.id = servo_id
    msg_rad.rad = rad
    for i in range(3):
        RAD_PUB.publish(msg_rad)
        r.sleep()
    msg_spd = servo_speed()
    msg_spd.id = servo_id
    msg_spd.speed = spd
    for i in range(3):
        SPE_PUB.publish(msg_spd)
        r.sleep()

