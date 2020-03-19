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
#import okaovision

## 2. HEAD MODULE ##
#import head

## 3. SPEECH MODULE ##
#import speech
import threading

## OTHER... ##
#from shared import Shared
import time
import numpy as np
import random

#from shared import Shared



#音声関係のライブラリ
import pyaudio


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
        if m > 200:
            print("!!!", m)


#### メイン ####
def main():
    ## 0. INIT ROS... ##
    rospy.init_node('subscriber', anonymous=True)

    audio_loop = threading.Thread( target=audioLoop)
    audio_loop.daemon = True
    audio_loop.start()
    
    rospy.spin()
   


if __name__=="__main__":
    main()
