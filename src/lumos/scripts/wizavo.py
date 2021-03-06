#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# created by: tatsumi
#
import rospy
from srv_test.srv import *


def add_two_ints_client(data):
    rospy.wait_for_service('test_topic')
    try:
        method = rospy.ServiceProxy('test_topic', test)
        resp1 = method(data)
        return resp1.res
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


def wav(data):
    DIR = "/home/icduser/catkin_ws/src/srv_test/scripts/"
    return DIR + add_two_ints_client(data)
