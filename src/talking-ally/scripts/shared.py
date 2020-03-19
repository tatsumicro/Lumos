#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# created by: tatsumi
#
import numpy as np

class Shared():
    ## eye and face... ##
    EYE_X = EYE_Y = FACE_X = FACE_Y = 0.0

    ## gazing and addressing... ##
    LR = np.array([0] * 5)
    UD = np.array([0] * 5)
    gazeLR = np.array([0] * 5)
    gazeUD = np.array([0] * 5)
    preLR = 0.0
    preUD = 0.0
    preGazeLR = 0.0
    preGazeUD = 0.0

    ## speech... ##
    isAttention = True
    isLookingAwayEye = True
    isLookingAwayFace = True
    isExit = False
    isExit_before = False

    nod = False

    attentionCnt = 0
