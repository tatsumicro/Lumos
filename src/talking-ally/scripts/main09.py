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
	
	
	def __init__(self, okaomanager):
		self.okaomanager = okaomanager
		servo.init()
	
	
	def start_updateLoop(self):
		threads = [
			self.addressLoop, # 人の方を向く
			self.musicRecognizeLoop, # 音に反応
			#self.voiceRecognizeLoop, # 声に反応
			self.findingLoop, # 人がいない時に探すしぐさ
			self.lightControllLoop
			]
		for thread in threads:
			update_loop = threading.Thread( target=thread )
			update_loop.daemon = True
			update_loop.start()
	
	
	darkness = 1
	COOL = [20/darkness, 100/darkness, 100/darkness, 0]
	WARM = [200/darkness, 240/darkness, 160/darkness, 0]
	def lightControllLoop(self):
		"""
		動作：　人との距離でライトを制御する
		"""
		notice = '[Interaction]: lightControllLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))
		
		port = "/dev/ttyACM1"
		baudrate = 115200
		led = serialled.SerialLed(port, baudrate)
		color = [0, 0, 0, 0]
		closer = 300
		far = 100
		while True:
			if not self.okaomanager.isExist(): # 人がいない
				for i in range(4):
					color[i] = self.COOL[i]
				led.setColor(color[0], color[1], color[2], color[3])
				led.setColor(color[0], color[1], color[2], color[3])
			else:
				for i in range(4):
					color[i] = self.WARM[i]
				led.setColor(color[0], color[1], color[2], color[3])
				led.setColor(color[0], color[1], color[2], color[3])
				pass
			"""
			key = okaomanager.getMaxAttentionKey("size")
			size = okaomanager.getAttension(key, "size")
			#print(size)
			size = min(closer, max(far, size))
			
			size_rate = 1.0*(size-far)/(closer-far) # 近いと1.0、遠いと0.0
			for i in range(4):
				color[i] = int(self.WARM[i]*size_rate + self.COOL[i]*(1-size_rate))
			led.setColor(color[0], color[1], color[2], color[3])
			led.setColor(color[0], color[1], color[2], color[3])
			"""
			time.sleep(0.1)
			
	
	def findingLoop(self):
		"""
		動作：　誰もいない時に見渡す
		"""
		notice = '[Interaction]: findingLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))
		
		while True:
			if not self.okaomanager.isExist(): # 人がいない
				radx = self.pos[4]
				rady = self.pos[3]
				rand1 = random.random()-0.5
				rand2 = random.random()-0.5
				radx += rand1
				speed = 0.3
				self.address_rad(-0.5+rand1*0.5, 0.0+rand2*0.5, 0.7, update=False)
				time.sleep(0.7)
			else:
				radx = self.pos[4]
				rady = self.pos[3]
				rand1 = random.random()-0.5
				rand2 = random.random()-0.5
				radx += rand1*200
				radx = min(1200, max(radx, 0))
				rady = min(1200, max(rady, 0))
				self.address_rad(radx, rady, 0.5, update=False)
				time.sleep(0.7)
				pass
			
			
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
				sleep = 1
				rand = (random.random()-0.5) * 100
				self.address(x, 700, sleep)
			time.sleep(0.2)
			
	
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
		notice = '[Interaction]: musicRecognizeLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))
		
		CHUNK = 512
		RATE = 16000
		p = pyaudio.PyAudio()
		stream = p.open(format=pyaudio.paInt16, channels=1, frames_per_buffer=CHUNK, rate=RATE, input=True)
		buf = np.array([0.0] * self.AUDIOBUFFSIZE)
		while True:
			data = stream.read(CHUNK)
			data = np.frombuffer(data, offset=0, dtype="int16")
			data = np.abs(data)
			m = np.mean(data)
			ave = np.average(buf) # 平均
			if ave + 10.0 < m:
				speed = 0.9
				self.standup(0.3, speed)
			else:
				speed = 0.6
				self.standup(0.2, speed)
			buf = self.queue(buf, m)
			
			
	def voiceRecognizeLoop(self):
		notice = '[Interaction]: voiceRecognizeLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))
		
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
			if 170 < m:
				speed = 0.9
				self.standup(0.7, speed)
			if 140 < m:
				speed = 0.7
				self.standup(0.3, speed)
			else:
				speed = 0.5
				self.standup(0.2, speed)
			#buf = self.queue(buf, m)
			
		
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
	
	
