#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# update: 2019/08/30
# created by: tatsumi
#

import termcolor
import rospy
from okao.msg import *
import numpy as np

import threading
import time


#------------------------------#
# OkaoVisionManager Class      #
#------------------------------#
class OkaoVisionManager:
	"""
	OkaoVisionで検知したデータの2次的要素を扱います。
	例えば、顔の傾きのログ、視線のログなど時間的要素を含んでいます。
	"""
	okaomonitor = None
	people = None
	
	# キューの更新周期
	SLEEPTIME = 0.05
	
	# ie. {"LR": {11: array(-50, ...), 12: array(-30, ...)}}
	ATTE_TYPES = ["x", "y", "size", "LR", "UD", "gazeLR", "gazeUD"]
	BUFFSIZE = 5 # キューのサイズ
	attention_list = {}
	

	def __init__(self, okaomonitor):
		self.okaomonitor = okaomonitor
		
		for atte_type in self.ATTE_TYPES:
			self.attention_list[atte_type] = {}
		
		notice_init = '[OkaoVisionManager init]: Initialization Compete!\n'
		print(termcolor.colored(notice_init, 'green'))
		
	
	def start_updateLoop(self):
		update_loop = threading.Thread( target=self.updateLoop)
		update_loop.daemon = True
		update_loop.start()
		
		
	def updateLoop(self):
		"""
		OkaoVisionのデータからログを取ります。
		"""
		notice = '[OkaoVisionManager]: updateLoop start!\n'
		print(termcolor.colored(notice, 'yellow'))
		
		while True:
			self.people = self.okaomonitor.getAll()
			#print("***")
			#print(self.people)
			
			# キューを更新
			for atte_type in self.ATTE_TYPES:
				self.updateAttentionLog(self.people, atte_type)
				
			#x, y = self.getMaxAttensionFaceXY("LR")
			#print(x, y)
			time.sleep(self.SLEEPTIME)

	
	def isExist(self):
		return len(self.people) > 0
		
	
	def getAttension(self, key, attentionType):
		# 引数の属性値を返す。
		if not key in self.people:
			return 0.0
		return self.people[key][attentionType]
		
	
	def getFaceXY(self, key):
		if not key in self.people:
			return (0, 0)
		return (self.people[key]["x"], self.people[key]["y"])
		
		
	def getMaxAttensionFaceXY(self, attentionType):
		"""
		引数の属性値が最も大きい人の位置を返す。
		最もサイズが大きい人の位置（x, y）など。
		"""
		key = self.getMaxAttentionKey(attentionType)
		return self.getFaceXY(key)
		
		
	def getMinAttensionFaceXY(self, attentionType):
		"""
		引数の属性値が最も小さい人の位置を返す。
		最もサイズが小さい人の位置（x, y）など。
		"""
		key = self.getMinAttentionKey(attentionType)
		return self.getFaceXY(key)
		
		
	def getMaxAttentionKey(self, attentionType):
		"""
		引数の属性値が最も大きい人のIDを返す。
		"""
		ave_dic = {-1:-10000} # 誰もいない時はID=-1を返す。
		for key in self.attention_list[attentionType].keys():
			ave_dic[key] = np.average(self.attention_list[attentionType][key])
		return max([(v,k) for k,v in ave_dic.items()])[1]
		
		
	def getMinAttentionKey(self, attentionType):
		"""
		引数の属性値が最も小さい人のIDを返す。
		"""
		ave_dic = {-1:10000} # 誰もいない時はID=-1を返す。
		for key in self.attention_list[attentionType].keys():
			ave_dic[key] = np.average(self.attention_list[attentionType][key])
		return min([(v,k) for k,v in ave_dic.items()])[1]
				
	
	def updateAttentionLog(self, people, attentionType):
		"""
		検出した人の動作ログをキューに格納しておきます。
		"""
		# 検知していない人のIDはキューから除外する。キューがあふれるのを防止！！
		for key in self.attention_list[attentionType].keys():
			if not key in people:
				del self.attention_list[attentionType][key]
		
		#
		for key in people.keys():
			if not key in self.attention_list[attentionType]:
				self.attention_list[attentionType][key] = np.array([0] * self.BUFFSIZE)
			self.attention_list[attentionType][key] = \
				self.queue(self.attention_list[attentionType][key], people[key][attentionType])
			
			
	def queue(self, src, a):
		dst = np.roll(src, -1)
		dst[-1] = a
		return dst
		

#------------------------------#
# OkaoVisionMonitor Class      #
#------------------------------#
class OkaoVisionMonitor:
	SLEEPTIME = 0.05 # 0.05がちょうどいい
	
	# 統合するカメラ情報
	chattername_list = []
	okao_list = []
	
	people = {}
	

	def __init__(self, chattername_list, offset_list):
		self.chattername_list = chattername_list
		self.offset_list = offset_list
		
		if len(chattername_list) != len(offset_list):
			# Notice...
			notice_init_error = '[OkaoVisionMonitor init] Error: Arguments size are wrong...'
			print(termcolor.colored(notice_init_error, 'red'))
			
		for chattername in self.chattername_list:
			self.okao_list += [OkaoVision(chattername, offset_list[chattername])]
		
		# Notice...
		notice_init = '[OkaoVisionMonitor init]: Initialization Compete!\n'
		notice_init += " * chatter="+str(chattername_list)+"\n"
		print(termcolor.colored(notice_init, 'green'))
		
		
	def start_updateLoop(self):
		update_loop = threading.Thread( target=self.updateLoop)
		update_loop.daemon = True
		update_loop.start()
		
		
	def updateLoop(self):
		while True:
			self.updateOkao()
			# self.printAll()
			time.sleep(self.SLEEPTIME)
	
	
	# 検出しているすべての人を返す。
	def getAll(self):
		return self.people
		
				
	def updateOkao(self):
		self.people = {}
		
		for i in range(len(self.okao_list)):
			# edit people xy offset.
			raw_people = self.okao_list[i].getAll()
			self.people.update(raw_people)
	
	
	def printAll(self):
		for key in self.people.keys():
			human = self.people[key]
			showdata = np.array([key, human["x"], human["y"], human["LR"]])
			#showdata = np.array([human["LR"], human["gazeLR"]])
			notice = str(showdata)+"\n"
			print(termcolor.colored(notice, 'yellow'))
		print(termcolor.colored("==========\n\n", 'yellow'))
		

#------------------------------#
# OkaoVision Class             #
#------------------------------#
class OkaoVision:
	people = {}
	offset = None
	

	def __init__(self, chattername, offset):
		rospy.Subscriber(chattername, face_info, self.callback)
		self.offset = offset
		
		# print LOG...
		notice_init = '[OkaoVision init]: Initialization Compete!\n'
		notice_init += ' * \''+chattername+'\'\n'
		print(termcolor.colored(notice_init, 'green'))


	# 検出しているすべての人を返す。
	def getAll(self):
		return self.people


	def callback(self, msg):
		#notice = '[OkaoVision callback]: \n'
		#notice += ' * msg.face_count='+str(msg.face_count)+'\n'
		#print(termcolor.colored(notice, 'yellow'))

		# There is No people...
		if msg.face_count==0:
			self.people = {}
			pass
		# Hey, people!
		else:
			self.people = {}
			for idx in range(msg.face_count):
				self.people[msg.id[idx]] = self.getHuman(msg, idx)
			pass


	def getHuman(self, msg, idx):
		if idx>=0 & idx<msg.face_count & msg.face_count==0:
			return None
		else:
			human = {
				"id": msg.id[idx],\
				"x": msg.x[idx] + self.offset["x"],\
				"y": msg.y[idx] + self.offset["y"],\
				"size": msg.size[idx],\
				"LR": msg.LR[idx] + self.offset["LR"],\
				"UD": msg.UD[idx] + self.offset["UD"],\
				"gazeLR": msg.gazeLR[idx] + self.offset["gazeLR"],\
				"gazeUD": msg.gazeUD[idx] + self.offset["gazeUD"]}
			return human


if __name__ == '__main__':
	rospy.init_node('subscriber', anonymous=True)
	
	chatterlist = ['chatter_left', 'chatter_right']
	offsetlist = [{"x":-1000, "y":+0, "LR":+0, "gazeLR":0, "UD":+0, "gazeUD":0}, \
					{"x":-540, "y":+0, "LR":-0, "gazeLR":0, "UD":+0, "gazeUD":0}]
	okaomonitor = OkaoVisionMonitor(chatterlist, offsetlist)
	okaomonitor.start_updateLoop()
	
	rospy.spin()
	
