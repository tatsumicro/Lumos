# -*- coding: UTF-8 -*-
#
# update: 2018/07/19 
# created by: tatsumi
#
#!/usr/bin/env python

import rospy

# subprocess
import subprocess


if __name__ == "__main__":
    print "#################################"
    dirc = "/home/icduser/catkin_ws/src/srv_test/script/"
    subprocess.call(dirc + "wiz_client", shell=True)
