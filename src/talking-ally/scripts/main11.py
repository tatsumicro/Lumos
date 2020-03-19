#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# update: 2018/08/06 すべてのmoduleを統合
# created by: tatsumi
#
# multiplayer and ally interaction...
#

# Built-in/Generic Imports
import json
import threading
import time
import random

# Libs
import rospy
import termcolor
import serial
import numpy as np
import pyaudio

# Own modules
import okaovision
import servo
import serialled

import speech


#------------------------------#
# Interaction                  #
#------------------------------#
class Interaction:
	AUDIOBUFFSIZE = 10
	okaomanager = None
	
	# 現在の位置
	pos = {1:0, 2:0, 3:0, 4:0}
	state_flag = [ False, False, False, False ]

	def __init__(self, okaomanager=None):
		speech.init()
		pass


	def start_updateLoop(self):
		threads = [
			#self.addressLoop, # 人の方を向く
			speech.actionLoop,
			]
		for thread in threads:
			update_loop = threading.Thread( target=thread )
			update_loop.daemon = True
			update_loop.start()


	def voiceRecognizeLoop(self):
		
		while True:
			data = stream.read(CHUNK)
			data = np.frombuffer(data, offset=0, dtype="int16")
			data = np.abs(data)
			m = np.mean(data)
			d = m-prem
			#self.state_flag = [False, False, False, False]
			#print(":: ", m)
			if 1200 < m:
				if 400 < d:
					state = 1
					self.state_flag[1] = True
				else:
					state = 2
					self.state_flag[2] = True
			else:
				if 400 < d:
					state = 3
					self.state_flag[3] = True
				else:
					state = 0
					self.state_flag[0] = True
			prem = m
			#print(":: ", self.state_flag)


#------------------------------#
# Main                         #
#------------------------------#
if __name__ == '__main__':
	rospy.init_node('subscriber', anonymous=True)
	
	print("test")
	interaction = Interaction()
	interaction.start_updateLoop()

	rospy.spin()
