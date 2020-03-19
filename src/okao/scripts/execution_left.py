#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import execution

if __name__ == '__main__':
	node = "talker"
	chatter =  "chatter_left"
	port = "/dev/ttyACM0"
	try:
		execution.main( node, chatter, port )
	except rospy.ROSInterruptException:
		pass
