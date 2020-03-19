#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# update: 2018/08/06 すべてのmoduleを統合 
# created by: tatsumi
#

# ros
import sys
import rospy

## WIZAVO MODULE ##
import wizavo

## MECAB MODULE ##
import mecab

# pygame
import pygame.mixer
from pygame.locals import *

# thread...
import time
import threading
import random

from shared import Shared


#------------------------------#
# SpeechManager Class          #
#------------------------------#
class SpeechManager:
	def __init__(self, okaomonitor):
		self.okaomonitor = okaomonitor
		
		for atte_type in self.ATTE_TYPES:
			self.attention_list[atte_type] = {}
		
		notice_init = '[SpeechManager init]: Initialization Compete!\n'
		print(termcolor.colored(notice_init, 'green'))
		
	
	def start_updateLoop(self):
		update_loop = threading.Thread( target=self.updateLoop)
		update_loop.daemon = True
		update_loop.start()


def init():
    print "speech initialization..."
    pygame.mixer.pre_init(16000, 16, 2, 1024 * 4)
    pygame.init()


def getModalityList( string ):
    res = mecab.parse( string )
    modlist = []
    phrase = ""
    for item in res:
        if item[1] == "助詞":
            phrase += item[len(item) - 1]
            phrase += "ね"
            modlist.append(phrase)
            phrase = ""
        elif item[1] == "記号":
            if len(phrase) > 0:
                if item[0] == "、":
                    phrase += "ね"
                if item[0] == "。":
                    phrase += "よ"
                modlist.append(phrase)
            phrase = ""
        else:
            phrase += item[len(item) - 1]
    return modlist


def speak( word ):
    print("speak...start...")
    filler = pygame.mixer.Sound( wizavo.wav( word ) )
    
    filler.play()
    print("len=", filler.get_length())
    time.sleep( filler.get_length() )
    print("speak...end...")
    

def filler():
    fillers = [ "えっと", "その", "あの" ]
    i = 0
    while Shared.isLookingAwayEye or Shared.isLookingAwayFace:
        t = 0.5
        tp = 0.1
        while t > 0:
            if Shared.isLookingAwayEye == False and Shared.isLookingAwayFace == False:
                return 0
            t = t - tp
            time.sleep( tp )
        speak( fillers[i] )
        i = (i + 1) % len(fillers)
        t = 5.0
        tp = 0.1
        while t > 0:
            if Shared.isLookingAwayEye == False and Shared.isLookingAwayFace == False:
                return 0
            t = t - tp
            time.sleep( tp )


def my_play( wavfile ):
    hoge = pygame.mixer.Sound( wavfile )
    l = hoge.get_length()
    ll = l
    tp = 0.1
    hoge.play()
    while ll > 0:
        #print Shared.isLookingAwayEye
        if Shared.isLookingAwayEye == False and Shared.isLookingAwayFace == False:
            time.sleep(tp)
            ll = ll - tp
        else:
            Shared.isAttention = False
            hoge.fadeout(500)
            time.sleep(0.5)
            #hoge.stop()
            filler()
            Shared.isAttention = True
            #speak( "それでね" )
            hoge.play()
            ll = l
    Shared.nod = True
    time.sleep(1)
    Shared.nod = False

    # 言いよどみをする？
    print Shared.attentionCnt
    if Shared.attentionCnt > 4:
        speak("それでね")
    else:
        ano = ["あの", "その", "", "", ""]
        fil = ano[random.randrange(len(ano))]
        if len(fil) > 0:
            speak(fil)
    Shared.attentionCnt = 0
    time.sleep(0.5)


def actionLoop():
	file = open('/home/icd/catkin_ws/src/talking-ally/scripts/story.txt', 'r')
	string = file.read()
	modlist = getModalityList( string )
	
	for word in ["Hello", "bye", "Momotaro"]:
		if (rand(1000000) == 0):
			wasureta()
		speak( word )


def wasureta( word ):
	similar = simi( word )
	for similar in ["Hello", "bye", "Momotaro"]:
		if (rand(1000000) == 0):
			wasureta()
		speak( word )




