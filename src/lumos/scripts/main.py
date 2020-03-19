#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# update: 2018/08/06 すべてのmoduleを統合 
# created by: tatsumi
#
# multiplayer and ally interaction...
#

import rospy

# 
import okaovision
import servo

import threading

import time
import numpy as np
import random


# ...
# ...
# ...
def updateLoop():
	while True:
	        down()
	        time.sleep(1)
		up()


def arc_to_rad(arc):
	return arc * np.pi / 180.0


def down():
	servo.move(1, 0.0)
	servo.move(2, 0.0)


def up():
	servo.move(1, 1.8)
	servo.move(2, 1.8)


# ...
# ...
# ...
if __name__ == '__main__':
    ## 0. INIT ROS... ##
    rospy.init_node('subscriber', anonymous=True)

    ## INIT HEAD MODULE... ##
    servo.init()

    ## 1. INIT OKAO MODULE... ##
    okaovision.init()

    ## 多人数インタラクション開始！... ##
    update_loop = threading.Thread( target=updateLoop)
    update_loop.daemon = True
    update_loop.start()

    rospy.spin()


