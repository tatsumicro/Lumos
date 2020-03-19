#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# update: 2018/08/06 すべてのmoduleを統合 
# created by: tatsumi
#
# multiplayer and ally interaction...
#

import termcolor
import rospy

import okaovision
import head

import threading

import time
import numpy as np
import random

import pyaudio

import servo


#------------------------------#
# Interaction                  #
#------------------------------#
class Interaction:
	okaomanager = None
	# サーボのオフセット
	offsetlist = [{"x":-1000, "y":+0, "LR":+0, "gazeLR":0, "UD":+0, "gazeUD":0}, \
					{"x":-540, "y":+0, "LR":-0, "gazeLR":0, "UD":+0, "gazeUD":0}]
	
	
	def __init__(self, okaomanager):
		self.okaomanager = okaomanager
		servo.init()
	
	
	def start_updateLoop(self):
		update_loop = threading.Thread( target=self.actionLoop)
		update_loop.daemon = True
		update_loop.start()
		
		update_loop1 = threading.Thread( target=self.addressLoop)
		update_loop1.daemon = True
		update_loop1.start()
		
	
	def addressLoop(self):
		"""
		動作：　人の方を向く動作
		"""
		notice = '[Interaction]: addressLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))
		
		while True:
			x, y = self.okaomanager.getMaxAttensionFaceXY("size")
			self.address(x, y)
			time.sleep(0.1)
			pass
			
	
	def xy_to_rad(self, x, y):
		return (0.0-1.0*x/600, -1.0+1.0*y/480)
		
		
	def address(self, x, y):
		radx, rady = self.xy_to_rad(x, y)
		#print("x="+str(x), "y="+str(y))
		#print("radx="+str(radx), "rady="+str(rady))
		servo.move(4, radx)
		servo.move(3, rady)
		
	
	def audioLoop():
    # define...
    CHUNK = 512
    RATE = 16000

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, frames_per_buffer=CHUNK, rate=RATE, input=True)

    while True:
        data = stream.read(CHUNK)
        data = np.frombuffer(data, offset=0, dtype="int16")
        data = np.abs(data)
        m = np.mean(data)
        if m > 170:
            #print("!!!", m)
            head.sit(0.7)
        else:
            #print("!!!", m)
            head.sit()
            
	
	def actionLoop(self):
		"""
		...??
		"""
		notice = '[Interaction]: addressLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))
		
		while True:
			pass
			time.sleep(0.1)
		
		
#------------------------------#
# Main                         #
#------------------------------#
if __name__ == '__main__':
	rospy.init_node('subscriber', anonymous=True)
	
	chatterlist = ['chatter_left', 'chatter_right']
	offsetlist = {"chatter_left": {"x":-1000, "y":+0, "LR":+0, "gazeLR":0, "UD":+0, "gazeUD":0}, \
					"chatter_right": {"x":-540, "y":+0, "LR":-0, "gazeLR":0, "UD":+0, "gazeUD":0}}
	okaomonitor = okaovision.OkaoVisionMonitor(chatterlist, offsetlist)
	okaomonitor.start_updateLoop()
	
	okaomanager = OkaoVisionManager(okaomonitor)
	okaomanager.start_updateLoop()
	
	interaction = Interaction(okaomanager)
	interaction.start_updateLoop()
	
	rospy.spin()
	
	
