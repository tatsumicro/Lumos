#!/usr/bin/env python


import sys
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


def usage():
    return "%s [data]"%sys.argv[0]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        data = str(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "Requesting %s"%(data)
    print "%s -> %s"%(data, add_two_ints_client(data))
