#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# update: 2019/08/30
# created by: tatsumi
#
#

## ROS ##
import rospy

## I/O module ##
import okaovision
import head

## Other ##
import threading
import time
import numpy as np
import random

# OkaoVisionの画角
height_max = 1400

# 正面に来た時に0になるように調整！
margin_x0 = -1087
margin_x1 = -400
margin_y0 = 100
margin_y1 = 0
	
class Interaction:
	okao0 = None
	okao1 = None
	people0 = {}
	people1 = {}
	x0 = []
	x1 = []
	y0 = []
	y1 = []
	gazeLog = {}
	addrLog = {}


	def __init__(self):
		self.okao0 = okaovision.OkaoVision("chatter_okao0")
		self.okao1 = okaovision.OkaoVision("chatter_okao1")
		pass
		
		
	def startAllThread(self):
		threadmethod = [ self.updateLoop, self.outputLoop ]
		for threaditem in threadmethod:
			threadloop = threading.Thread( target=threaditem )
			threadloop.daemon = True
			threadloop.start()


	def updateLoop(self):
		while True:
			self.people0 = self.okao0.getAll()
			self.people1 = self.okao1.getAll()
			
			self.x0 = []
			self.y0 = []
			for item in self.people0.values():
				self.x0.append(item["x"] + margin_x0)
				self.y0.append(height_max/2 - item["y"] + margin_y0)
			self.x1 = []
			self.y1 = []
			for item in self.people1.values():
				self.x1.append(item["x"] + margin_x1)
				self.y1.append(height_max/2 - item["y"] + margin_y1)
			
			x = self.x0
			x.extend(self.x1)
			y = self.y0
			y.extend(self.y1)
			
			xy = []
			for i in range(len(x)):
				xy.append((x[i], y[i]))
				
			print("**********")
			print(xy)
			
			time.sleep(0.01)
			
			
	def outputLoop(self):
		while True:
			#print("0 >> ", self.xy0)
			#print("1 >> ", self.xy1)
			time.sleep(0.01)


if __name__ == '__main__':
	rospy.init_node('subscriber', anonymous=True)
	
	interaction = Interaction()
	interaction.startAllThread()
	
	rospy.spin()
