#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# update: 2019/07/09 すべてのmoduleを統合 
# created by: tatsumi
#
# Nod detection test.
#

## ROS ##
import rospy

## OKAO MODULE ##
import okaovision

## HEAD MODULE ##
import head

## SPEECH MODULE ##
import threading

## OTHER... ##
from shared import Shared
import time
import numpy as np
from scipy import interpolate
import random

from shared import Shared

##
import pyaudio

#プロット関係のライブラリ
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import sys

#音声関係のライブラリ
import pyaudio
import struct


## ...!... ##
class PlotWindow:
    global pre

    def __init__(self):
        global pre
        pre = 0

        #プロット初期設定
        self.win=pg.GraphicsWindow()
        self.win.setWindowTitle(u"リアルタイムプロット")
        self.plt=self.win.addPlot() #プロットのビジュアル関係
        self.plt.setYRange(-25,25)    #y軸の上限、下限の設定
        self.curve=self.plt.plot()  #プロットデータを入れる場所

        #マイクインプット設定
        self.CHUNK=20             #1度に読み取る音声のデータ幅
        #self.RATE=44100             #サンプリング周波数
        #self.audio=pyaudio.PyAudio()
        #self.stream=self.audio.open(format=pyaudio.paInt16,
        #                           channels=1,
        #                           rate=self.RATE,
        #                           input=True,
        #                           frames_per_buffer=self.CHUNK)

        #アップデート時間設定
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)    #10msごとにupdateを呼び出し

        #音声データの格納場所(プロットデータ)
        self.data=np.zeros(self.CHUNK)

    def update(self):
        dx = self.input()
        self.data=np.append(self.data, dx)
        if len(self.data) > self.CHUNK:     #5*1024点を超えたら1024点を吐き出し
            self.data=self.data[len(self.data)-self.CHUNK:]
        # 補間
        x = np.linspace(0, self.CHUNK, self.CHUNK)
        y = self.data
        #x = np.array([0, 1, 2, 3, 4])
        #y = np.array([0, 50, 70, 0, 90])
        #print("scipy::", type(y[0]))
        f = interpolate.interp1d(x, y, kind='cubic')

        x = np.linspace(0, self.CHUNK, self.CHUNK * 100)
        newy = f(x)
        #print("scipy::", newy)
        #self.data=np.array(newy)
        
        self.curve.setData(newy)   #プロットデータを格納


    def input(self):
        global pre
        buf = okaovision.get()
        if buf == 0:
            pre = 0
            return 0
        else:
            res = (buf - pre)
            pre = buf
            if abs(res) > 5:
                return res
            return 0



class PlotWindowAnalysis:
    global pre

    def __init__(self):
        global pre
        pre = 0

        #マイクインプット設定
        self.CHUNK=20            #1度に読み取る音声のデータ幅
        self.RATE=100             #サンプリング周波数
        self.update_seconds=50      #更新時間[ms]
        self.audio=pyaudio.PyAudio()

        #音声データの格納場所(プロットデータ)
        self.data=np.zeros(self.CHUNK)
        self.axis=np.fft.fftfreq(len(self.data), d=1.0/self.RATE)

        #プロット初期設定
        self.win=pg.GraphicsWindow()
        self.win.setWindowTitle("SpectrumAnalyzer")
        self.plt=self.win.addPlot() #プロットのビジュアル関係
        self.plt.setYRange(0, 80)    #y軸の制限

        #アップデート時間設定
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(self.update_seconds)    #10msごとにupdateを呼び出し


    def update(self):
        dx = self.input()
        if True:
            self.data=np.append(self.data, dx)
            if len(self.data) > self.CHUNK:     #5*1024点を超えたら1024点を吐き出し
                self.data=self.data[len(self.data)-self.CHUNK:]
        # 補間
        x = np.linspace(0, self.CHUNK, self.CHUNK)
        y = self.data
        f = interpolate.interp1d(x, y, kind='cubic')

        x = np.linspace(0, self.CHUNK, self.CHUNK * 100)
        newy = f(x)

        self.fft_data = self.FFT_AMP(self.data)

        self.axis=np.fft.fftfreq(len(self.data), d=1.0/self.RATE)
        self.plt.plot(x=self.axis, y=self.fft_data, clear=True, pen="y")  #symbol="o", symbolPen="y", symbolBrush="b")


    def FFT_AMP(self, data):
        data=np.hamming(len(data))*data
        data=np.fft.fft(data)
        data=np.abs(data)
        return data


    def input(self):
        global pre
        buf = okaovision.get()
        if buf == 0:
            pre = 0
            return 0
        else:
            res = (buf - pre)
            pre = buf
            if abs(res) > 5:
                return res
            return 0


## ...Main... ##
if __name__=="__main__":
    ## ...INIT ROS... ##
    rospy.init_node('subscriber', anonymous=True)

    ## ...INIT OKAO MODULE... ##
    okaovision.init()

    ## ...Plot... ##
    plotwin=PlotWindowAnalysis()
    plotwin2=PlotWindow()
    if (sys.flags.interactive!=1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()


    rospy.spin()

