#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# update: 2018/08/06 すべてのmoduleを統合 
# created by: tatsumi
#
# multiplayer and ally interaction...
#

## 0. ROS ##
import rospy

## 1. OKAO MODULE ##
import okaovision

## 2. HEAD MODULE ##
import head

## 3. SPEECH MODULE ##
#import speech
import threading

## OTHER... ##
from shared import Shared
import time
import numpy as np
import random

from shared import Shared

##
import pyaudio



			

global HEARER
HEARER = None
### Loop: 聞き手を探して顔を向ける ###
def findHearerLoop():
    global HEARER
    old_hearer = None
    old_id = -1
    cntdwn = 0
    while True:
        HEARER, i = getGoodListener(PEOPLE, ADDR_LOG)

        if cntdwn == 0:
            # 誰か居るから向く．．．
            if not HEARER is None:
                addressing(HEARER)
                old_hearer = HEARER
                old_id = i
                cntdwn = 25
            # 誰も居ない．．．
            else:
                pass
        elif old_id == i:
            if not HEARER is None:
                addressing(HEARER)
        
        cntdwn = max(0, cntdwn - 1)

        #print cntdwn

        time.sleep(0.1)


### Loop: 聞き手の目を見る　＆　時々よそ見 ###
def gazingLoop():
    while True:
        if not HEARER is None:
            if HEARER["id"] in PEOPLE:
                attention(HEARER["id"], GAZE_LOG, ADDR_LOG)
        time.sleep(0.4)


# 気になる方(x, y)を返す
def getInterestingTerget(i, att_gaze_x, att_x):
    Shared.isLookingAwayEye = False
    Shared.isLookingAwayFace = False

    left = (-0.1, 0.0)
    center = (0.0, 0.0)
    right = (0.1, 0.0)
    g_lr = np.average(att_gaze_x[i])
    lr = np.average(att_x[i])
    if lr < -15.0:
        Shared.isLookingAwayEye = True
        Shared.isLookingAwayFace = True
        return [d * 3 for d in right]
    if lr < -10.0:
        return [d * 2 for d in right]
    if lr < -5.0:
        return [d * 1 for d in right]
    if lr > 15.0:
        Shared.isLookingAwayEye = True
        Shared.isLookingAwayFace = True
        return [d * 3 for d in left]
    if lr > 10.0:
        return [d * 2 for d in left]
    if lr > 5.0:
        return [d * 1 for d in left]
    else:
        return (0.0, 0.0)



# 聞き手と共同注視
def attention(i, att_gaze_x, att_x):
    x, y = getInterestingTerget(i, att_gaze_x, att_x)
    gazingRelatively(x, y)


def queue(src, a):
    dst = np.roll(src, -1)
    dst[-1] = a
    return dst


# スタックアップデート
def updateAttentionX(people):
    global attentionX
    # delete old keys...
    for i in attentionX.keys():
        if not i in people:
            del attentionX[i]
    # add gazing data...
    for i in people.keys():
        if not i in attentionX:
            attentionX[i] = np.array([0] * 5)
        # print people[i]["LR"]
        attentionX[i] = queue(attentionX[i], people[i]["LR"])
    return attentionX


# スタックアップデート
def updateAttentionGazeX(people):
    global attentionGazeX
    # delete old keys...
    for i in attentionGazeX.keys():
        if not i in people:
            del attentionGazeX[i]
    # add gazing data...
    for i in people.keys():
        if not i in attentionGazeX:
            attentionGazeX[i] = np.array([0] * 5)
        attentionGazeX[i] = queue(attentionGazeX[i], people[i]["gazeLR"])
    return attentionGazeX


# 落ち着き度(con{...} or {})を返す
def getConcentration(attention):
    con = {}
    if len(attention) > 0:
        for i in attention.keys():
            con[i] = np.var(attention[i])
    return con


# 聞き手(human or None)を選んで返す
def getGoodListener(people, attention):
    con = getConcentration(attention)
    if len(con) > 0:
        min_k = min(con, key=con.get)
        return people[min_k], min_k
    return None, -1


#### 人の方に顔を向ける
def addressing(human):
    head.addressing(human["x"], human["y"]+300)
    pass


#### 人の方に目を向ける
def gazing(human):
    head.gazing(human["x"], human["y"]+300)
    pass


#### チラ見程度に使う
def gazingRelatively(x, y):
    head.gazingRelatively(x, y)
    pass


# 物音に反応する関数
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
            
            
def beatingLoop():
	rad = 0.2
	T = 0.1
	trad = T
	while True:
		head.sit(rad)
		rad = rad + trad
		if rad > 0.5:
			trad = -T
		if rad < 0.2:
			trad = T
		time.sleep(0.1)
		
		
def findingLoop():
	while True:
		HEARER, i = getGoodListener(PEOPLE, ADDR_LOG)
		if not HEARER is None:
			cnt = cnt + 1
		else:
			cnt = 0
		if cnt > 5:
			cnt = 0
			head.finding()
		time.sleep(0.1)
	

####
def main():
    global attentionGazeX
    attentionGazeX = {}

    global attentionX
    attentionX = {}

    ## 0. INIT ROS... ##
    rospy.init_node('subscriber', anonymous=True)

    ## INIT HEAD MODULE... ##
    head.init()

    ## 1. INIT OKAO MODULE... ##
    #okaovision.init()
    global okao
    okao = okaovision.OkaoVision("chatter_okao0")
    
    ## INIT SPEECH MODULE... ##
    #speech.init()
    #thread_speech = threading.Thread( target=speech.actionLoop )
    #thread_speech.daemon = True
    #thread_speech.start()

    ## 多人数インタラクション開始！... ##
    update_loop = threading.Thread( target=updateLoop)
    update_loop.daemon = True
    update_loop.start()
    
    findHearer_loop = threading.Thread( target=findHearerLoop)
    findHearer_loop.daemon = True
    findHearer_loop.start()

    gazing_loop = threading.Thread( target=gazingLoop)
    gazing_loop.daemon = True
    gazing_loop.start()

    audio_loop = threading.Thread( target=audioLoop)
    audio_loop.daemon = True
    audio_loop.start()
    
    ## 内なる鼓動 ##
    #beating_loop = threading.Thread( target=beatingLoop)
    #beating_loop.daemon = True
    #beating_loop.start()
    
    finding_loop = threading.Thread( target=findingLoop)
    finding_loop.daemon = True
    finding_loop.start()

    rospy.spin()
    

if __name__ == '__main__':
    main()


