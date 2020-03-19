#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# update: 2020/01/31 For a Experiment.
# created by: tatsumi
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
#import pyaudio

# Own modules
import okaovision
import servo
import serialled

#プロット関係のライブラリ
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
#import numpy as np
import sys

#音声関係のライブラリ
import pyaudio
import struct


#------------------------------#
# Parameter                    #
#------------------------------#
PORT = "/dev/ttyACM0"
BOUDRATE = 115200


#------------------------------#
# Interaction                  #
#------------------------------#
class Interaction:
	AUDIOBUFFSIZE = 20
	okaomanager = None
	# サーボのオフセット
	offsetlist = [{"x":-1000, "y":+0, "LR":+0, "gazeLR":0, "UD":+0, "gazeUD":0}, \
					{"x":-540, "y":+0, "LR":-0, "gazeLR":0, "UD":+0, "gazeUD":0}]

	# 現在の位置
	pos = {1:0, 2:0, 3:0, 4:0}

	#
	soundbuf = np.array([0.0] * AUDIOBUFFSIZE)


	def __init__(self, okaomanager):
		self.okaomanager = okaomanager
		servo.init()


	def start_updateLoop(self):
		threads = [
			#self.fluctuationLoop,
			#self.addressLoop, # 人の方を向く
			#self.musicRecognizeLoop, # 音に反応
			self.soundSensingLoop, # sensing sound
			self.objectLoop, # like a object.
			#self.voiceRecognizeLoop, # 声に反応
			#self.findingLoop, # 人がいない時に探すしぐさ
			self.lightControllLoop
			]
		for thread in threads:
			update_loop = threading.Thread( target=thread )
			update_loop.daemon = True
			update_loop.start()

		stateFunction = [
			self.stateSitting,
			self.stateStanding
		]
		time.sleep(1)
		stateFunction[self.state](1.0)
		stateFunction[self.state](1.0)


	darkness = 2
	COOL = [40/darkness, 130/darkness, 200/darkness, 100]
	WARM = [180/darkness, 100/darkness, 40/darkness, 60]
	def lightControllLoop(self):
		"""
		動作：　人との距離でライトを制御する
		"""
		notice = '[Interaction]: lightControllLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))

		port = "/dev/ttyACM1"
		baudrate = 115200
		led = serialled.SerialLed(port, baudrate)

		isOn = False
		while True:
			if self.state == 0 and isOn:
				led.setColor(10, 10, 10, 0)
				led.setColor(10, 10, 10, 0)
				isOn = False
				time.sleep(1)
			if self.state == 1 and not isOn:
				led.setColor(255, 255, 255, 0)
				led.setColor(255, 255, 255, 0)
				isOn = True
				time.sleep(1)



	def findingLoop(self):
		"""
		動作：　誰もいない時に見渡す
		"""
		notice = '[Interaction]: findingLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))

		while True:
			time.sleep(0.1)


	def addressLoop(self):
		"""
		動作：　人の方を向く動作
		"""
		notice = '[Interaction]: addressLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))

		while True:
			if self.state == 1:
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
				self.standup(0.5, speed)
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


	state = 0
	def objectLoop(self):
		"""
		Action: ?
		"""
		notice = '[Intetraction]: objectLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))

		self.state = 0
		stateFunction = [
			self.stateSitting,
			self.stateStanding
		]

		while True:
			ave = np.average(self.soundbuf)
			m = np.average(self.soundbuf[self.AUDIOBUFFSIZE-3:self.AUDIOBUFFSIZE-1])
			#m = self.soundbuf[self.AUDIOBUFFSIZE-1]
			#print(ave, m, m-ave)
			if self.state == 0:
				# sitting...
				if m - ave > 1300:
					self.state = 1
					stateFunction[self.state](0.8)
					time.sleep(1.1)
			elif self.state == 1:
				# standing...
				if m - ave > 1300:
					self.state = 0
					stateFunction[self.state](0.8)
					time.sleep(1.1)
			else:
				pass


	def stateSitting(self, speed, update=True):
		self.move(1, 0.1, speed, update)
		self.move(2, 0.1, speed, update)
		self.move(3, 0.7, speed, update)
		self.move(4, 0.0, speed, update)
		pass


	def stateStanding(self, speed, update=True):
		self.move(1, 0.6, speed, update)
		self.move(2, 0.6, speed, update)
		self.move(3, 0.4, speed, update)
		self.move(4, 0.0, speed, update)
		pass


	def soundSensingLoop(self):
		#--- NOTICE ---#
		notice = '[Interaction]: soundRecognizeLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))

		CHUNK = 512
		RATE = 16000
		p = pyaudio.PyAudio()
		stream = p.open(format=pyaudio.paInt16, channels=1, frames_per_buffer=CHUNK, rate=RATE, input=True)
		while True:
			data = stream.read(CHUNK)
			data = np.frombuffer(data, offset=0, dtype="int16")
			data = np.abs(data)
			m = np.mean(data)
			self.soundbuf = self.queue(self.soundbuf, m)
			#print(soundbuf)


class PlotWindow:
    def __init__(self):
        #マイクインプット設定
        self.CHUNK=1024            #1度に読み取る音声のデータ幅
        self.RATE=16000             #サンプリング周波数
        self.update_seconds=50      #更新時間[ms]
        self.audio=pyaudio.PyAudio()
        self.stream=self.audio.open(format=pyaudio.paInt16,
                                    channels=1,
                                    rate=self.RATE,
                                    input=True,
                                    frames_per_buffer=self.CHUNK)

        #音声データの格納場所(プロットデータ)
        self.data=np.zeros(self.CHUNK)
        self.axis=np.fft.fftfreq(len(self.data), d=1.0/self.RATE)

        #プロット初期設定
        self.win=pg.GraphicsWindow()
        self.win.setWindowTitle("SpectrumAnalyzer")
        self.plt=self.win.addPlot() #プロットのビジュアル関係
        self.plt.setYRange(0,100)    #y軸の制限

        #アップデート時間設定
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(self.update_seconds)    #10msごとにupdateを呼び出し

    def update(self):
        self.data=np.append(self.data,self.AudioInput())
        if len(self.data)/1024 > 10:
            self.data=self.data[1024:]
        self.fft_data=self.FFT_AMP(self.data)
        self.axis=np.fft.fftfreq(len(self.data), d=1.0/self.RATE)
        self.plt.plot(x=self.axis, y=self.fft_data, clear=True, pen="y")  #symbol="o", symbolPen="y", symbolBrush="b")

    def AudioInput(self):
        ret=self.stream.read(self.CHUNK)    #音声の読み取り(バイナリ) CHUNKが大きいとここで時間かかる
        #バイナリ → 数値(int16)に変換
        #32768.0=2^16で割ってるのは正規化(絶対値を1以下にすること)
        ret=np.frombuffer(ret, dtype="int16")/32768.0
        return ret

    def FFT_AMP(self, data):
        data=np.hamming(len(data))*data
        data=np.fft.fft(data)
        data=np.abs(data)
        return data


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

	#plotwin=PlotWindow()
	#if (sys.flags.interactive!=1) or not hasattr(QtCore, 'PYQT_VERSION'):
	#	QtGui.QApplication.instance().exec_()


	rospy.spin()
