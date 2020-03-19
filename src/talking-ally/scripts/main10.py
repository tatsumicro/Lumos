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


#------------------------------#
# Interaction                  #
#------------------------------#
class Interaction:
	AUDIOBUFFSIZE = 10
	okaomanager = None
	# サーボのオフセット
	offsetlist = [{"x":-1000, "y":+0, "LR":+0, "gazeLR":0, "UD":+0, "gazeUD":0}, \
					{"x":-540, "y":+0, "LR":-0, "gazeLR":0, "UD":+0, "gazeUD":0}]

	# 現在の位置
	pos = {1:0, 2:0, 3:0, 4:0}
	state_flag = [ False, False, False, False ]

	def __init__(self, okaomanager):
		global state
		state = 0
		#global state_flag
		state_flag = [ False, False, False, False ]
		self.okaomanager = okaomanager
		servo.init()


	def start_updateLoop(self):
		threads = [
			#self.addressLoop, # 人の方を向く
			self.musicRecognizeLoop, # 音に反応
			self.voiceRecognizeLoop, # 声に反応
			self.findingLoop, # 人がいない時に探すしぐさ
			#self.lightControllLoop
			]
		for thread in threads:
			update_loop = threading.Thread( target=thread )
			update_loop.daemon = True
			update_loop.start()


	darkness = 2
	COOL = [40/darkness, 130/darkness, 200/darkness, 100]
	WARM = [180/darkness, 100/darkness, 40/darkness, 60]
	def lightControllLoop(self):
		"""
		動作：　人との距離でライトを制御する
		"""
		notice = '[Interaction]: lightControllLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))

		port = "/dev/ttyACM0"
		baudrate = 115200
		led = serialled.SerialLed(port, baudrate)
		color = [0, 0, 0, 0]
		closer = 300
		far = 100
		while True:
			key = okaomanager.getMaxAttentionKey("size")
			size = okaomanager.getAttension(key, "size")
			#print(size)
			size = min(closer, max(far, size))

			size_rate = 1.0*(size-far)/(closer-far) # 近いと1.0、遠いと0.0
			for i in range(4):
				color[i] = int(self.WARM[i]*size_rate + self.COOL[i]*(1-size_rate))
			led.setColor(color[0], color[1], color[2], color[3])
			led.setColor(color[0], color[1], color[2], color[3])
			time.sleep(0.1)


	def findingLoop(self):
		"""
		動作：　誰もいない時に見渡す
		"""
		notice = '[Interaction]: findingLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))

		while True:
			servo.move(1, random.random(), 1)
			servo.move(2, random.random(), 1)

			x, y = self.okaomanager.getMaxAttensionFaceXY("size")
			if x == 0 and y == 0:
				servo.move(3, random.random(), 0.5)
				servo.move(4, random.random(), 0.5)
				pass
			else:
				sleep = 0.8
				self.address(x, y, sleep)
				
			time.sleep(0.1)



	def addressLoop(self):
		"""
		動作：　人の方を向く動作
		"""
		notice = '[Interaction]: addressLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))

		while True:
			x, y = self.okaomanager.getMaxAttensionFaceXY("size")
			if x == 0 and y == 0:
				pass
			else:
				sleep = 0.8
				self.address(x, y, sleep)
			time.sleep(0.1)


	def move(self, servo_id, rad, speed=1.0, update=True):
		if update:
			self.pos[servo_id] = rad
		servo.move(servo_id, rad, speed)


	def xy_to_rad(self, x, y):
		return (0.0-1.0*x/600, -1.0+1.0*y/480)


	def address_rad(self, radx, rady, speed=1.0, update=True):
		self.move(4, radx, speed, update)
		self.move(3, rady, speed, update)


	def address(self, x, y, speed=1.0):
		radx, rady = self.xy_to_rad(x, y)
		self.address_rad(radx, rady, speed)


	def standup(self, rad=0.1, speed=1.0):
		servo.move(1, rad, speed)
		servo.move(2, rad, speed)


	def queue(self, src, a):
		dst = np.roll(src, -1)
		dst[-1] = a
		return dst


	def musicRecognizeLoop(self):
		global state
		"""
		動作：　人との距離でライトを制御する
		"""
		notice = '[Interaction]: lightControllLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))

		port = "/dev/ttyACM2"
		baudrate = 115200
		led = serialled.SerialLed(port, baudrate)
		color = [0, 0, 0, 0]
		closer = 300
		far = 100
		while True:
			#print("state: ", state)
			print(":: ", self.state_flag)
			if self.state_flag[1]:
				print("action1")
				self.state_flag = [ False, False, False, False ]
				self.action1(led)
			elif self.state_flag[2]:
				print("action2")
				self.state_flag = [ False, False, False, False ]
				self.action2(led)
			elif self.state_flag[3]:
				print("action3")
				self.state_flag = [ False, False, False, False ]
				self.action3(led)
			elif self.state_flag[0]:
				print("action0")
				self.state_flag = [ False, False, False, False ]
				#self.action0(led)
			self.state_flag = [ False, False, False, False ]


	def action0(self, led):
		servo.move(1, 0.8, 1)
		servo.move(2, 0.8, 1)
		servo.move(3, 0.7, 1)
		servo.move(4, 0.5, 1)
		led.setColor(200, 255, 50, 10000)
		time.sleep(0.5)
		pass

	def action1(self, led):
		print("action1")
		servo.move(1, 1, 3)
		servo.move(2, 1, 3)
		servo.move(3, 0, 3)
		servo.move(4, 0.5, 3)
		led.setColor(255, 100, 50, 300)
		speed = 3
		x, y = self.okaomanager.getMaxAttensionFaceXY("size")
		self.address(x, y, speed)
		led.setColor(255, 100, 50, 300)
		time.sleep(3)
		pass

	def action2(self, led):
		servo.move(1, 1, 3)
		servo.move(2, 1, 3)
		servo.move(3, -1, 3)
		servo.move(4, (random.random()-0.5)*2 , 1)
		time.sleep(0.5)
		pass

	def action3(self, led):
		print("action1")
		servo.move(1, 1, 3)
		servo.move(2, 1, 3)
		servo.move(3, 0, 3)
		servo.move(4, 0.5, 3)
		led.setColor(255, 100, 50, 300)
		speed = 3
		x, y = self.okaomanager.getMaxAttensionFaceXY("size")
		self.address(x, y, speed)
		led.setColor(255, 100, 50, 300)
		time.sleep(3)
		pass


	def voiceRecognizeLoop(self):
		global state

		notice = '[Interaction]: voiceRecognizeLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))

		prem = 0

		CHUNK = 512
		RATE = 16000
		p = pyaudio.PyAudio()
		stream = p.open(format=pyaudio.paInt16, channels=1, frames_per_buffer=CHUNK, rate=RATE, input=True)
		#buf = np.array([0.0] * self.AUDIOBUFFSIZE)
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

	# OkaoVisionの設定
	"""
	chatterlist = ['chatter_left', 'chatter_right']
	offsetlist = {"chatter_left": {"x":-1000, "y":+0, "LR":+0, "gazeLR":0, "UD":+0, "gazeUD":0}, \
					"chatter_right": {"x":-540, "y":+0, "LR":-0, "gazeLR":0, "UD":+0, "gazeUD":0}}
	"""
	chatterlist = ['chatter_left', 'chatter_right']
	offsetlist = {"chatter_left": {"x":-1000, "y":+0, "LR":+0, "gazeLR":0, "UD":+0, "gazeUD":0}, \
					"chatter_right": {"x":-540, "y":+0, "LR":-0, "gazeLR":0, "UD":+0, "gazeUD":0}}

	okaomonitor = okaovision.OkaoVisionMonitor(chatterlist, offsetlist)
	okaomonitor.start_updateLoop()

	okaomanager = okaovision.OkaoVisionManager(okaomonitor)
	okaomanager.start_updateLoop()

	interaction = Interaction(okaomanager)
	interaction.start_updateLoop()

	rospy.spin()
