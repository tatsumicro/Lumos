#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import p2def
import B5Tdef
import STBdef
from serial_connector import SerialConnector
from hvc_p2_api import HVCP2Api
from hvc_tracking_result import HVCTrackingResult
from grayscale_image import GrayscaleImage
from operator import itemgetter

# 追加:ROS
import rospy
import random
from std_msgs.msg import String
from okao.msg import face_info


###############
# ユーザー定義 #
###############
# Output image file name.
img_fname = 'img.jpg'


# シリアル通信のタイムアウト時間(s)
# If you use UART slow baudrate, please edit here.
timeout = 30
###############

def _parse_arg(argv):
    argc = len(argv)
    if argc == 3 or argc == 4:
        # Gets port infomation
        portinfo = argv[1]
        # Gets baudrate
        baudrate = int(argv[2])
        if baudrate not in p2def.AVAILABLE_BAUD:
            print("Error: Invalid baudrate.")
            sys.exit()
        # Gets STB flag
        use_stb = p2def.USE_STB_ON # Default setting is ON
        if argc == 4 and argv[3] == "OFF":
            use_stb = p2def.USE_STB_OFF
    else:
        print("Error: Invalid argument.")
        sys.exit()
    return (portinfo, baudrate, use_stb)


def _check_connection(hvc_p2_api):
    (res_code, hvc_type, major, minor, release, rev) = hvc_p2_api.get_version()
    if res_code == 0 and hvc_type.startswith(b'B5T-007001'):
        pass
    else:
        raise IOError("Error: connection failure.")


def _set_hvc_p2_parameters(hvc_p2_api):
    # Sets camera angle
    res_code = hvc_p2_api.set_camera_angle(B5Tdef.hvc_camera_angle)
    if res_code is not p2def.RESPONSE_CODE_NORMAL:
        raise ValueError("Error: Invalid camera angle.")

    # Sets threshold
    res_code = hvc_p2_api.set_threshold(B5Tdef.body_thresh, B5Tdef.hand_thresh,\
                                        B5Tdef.face_thresh, B5Tdef.recognition_thresh)
    if res_code is not p2def.RESPONSE_CODE_NORMAL:
        raise ValueError("Error: Invalid threshold.")

    # Sets detection size
    res_code = hvc_p2_api.set_detection_size(B5Tdef.min_body_size, B5Tdef.max_body_size,\
                                             B5Tdef.min_hand_size, B5Tdef.max_hand_size,\
                                             B5Tdef.min_face_size, B5Tdef.max_face_size)
    if res_code is not p2def.RESPONSE_CODE_NORMAL:
        raise ValueError("Error: Invalid detection size.")

    # Sets face angle
    res_code = hvc_p2_api.set_face_angle(B5Tdef.face_angle_yaw, B5Tdef.face_angle_roll)
    if res_code is not p2def.RESPONSE_CODE_NORMAL:
        raise ValueError("Error: Invalid face angle.")


def _set_stb_parameters(hvc_p2_api):
    if hvc_p2_api.use_stb is not True:
        return

    # Sets tracking retry count.
    ret = hvc_p2_api.set_stb_tr_retry_count(STBdef.max_retry_count)
    if ret != 0:
        raise ValueError("Error: Invalid parameter. set_stb_tr_retry_count().")

    # Sets steadiness parameters
    ret = hvc_p2_api.set_stb_tr_steadiness_param(STBdef.steadiness_param_pos,
                                                 STBdef.steadiness_param_size)
    if ret != 0:
        raise ValueError("Error: Invalid parameter. set_stb_tr_steadiness_param().")

    #-- Sets STB parameters for Gender/Age estimation
    # Sets estimation result stabilizing threshold value
    ret = hvc_p2_api.set_stb_pe_threshold_use(STBdef.pe_threshold_use)
    if ret != 0:
        raise ValueError("Error: Invalid parameter. set_stb_pe_threshold_use().")

    # Sets estimation result stabilizing angle
    ret = hvc_p2_api.set_stb_pe_angle_use(STBdef.pe_min_UD_angle, STBdef.pe_max_UD_angle,\
                                          STBdef.pe_min_LR_angle, STBdef.pe_max_UD_angle)
    if ret != 0:
        raise ValueError("Error: Invalid parameter. set_stb_pe_angle_use().")

    # Sets age/gender estimation complete frame count
    ret = hvc_p2_api.set_stb_pe_complete_frame_count(STBdef.pe_complete_frame_count)
    if ret != 0:
        raise ValueError("Error: Invalid parameter. set_stb_pe_complete_frame_count().")

    #-- Sets STB parameters for Recognition
    # Sets recognition stabilizing threshold value
    ret = hvc_p2_api.set_stb_fr_threshold_use(STBdef.fr_threshold_use)
    if ret != 0:
        raise ValueError("Error: Invalid parameter. set_stb_fr_threshold_use().")

    # Sets recognition stabilizing angle
    ret = hvc_p2_api.set_stb_fr_angle_use(STBdef.fr_min_UD_angle, STBdef.fr_max_UD_angle,\
                                          STBdef.fr_min_LR_angle, STBdef.fr_max_LR_angle)
    if ret != 0:
        raise ValueError("Error: Invalid parameter. set_stb_fr_angle_use().")

    # Sets recognition stabilizing complete frame count
    ret = hvc_p2_api.set_stb_fr_complete_frame_count(STBdef.fr_complete_frame_count)
    if ret != 0:
        raise ValueError("Error: Invalid parameter. set_stb_fr_complete_frame_count().")

    # Sets recognition minimum account ratio
    ret = hvc_p2_api.set_stb_fr_min_ratio(STBdef.fr_min_ratio)
    if ret != 0:
        raise ValueError("Error: Invalid parameter. set_stb_fr_min_ratio().")


# in: hvc_tracking_result
# out: 
def getMsg(result):
    msg = face_info()
    msg.face_count = int(len(result.faces))
    for face in result.faces:
        msg.id.append(face.tracking_id)
        msg.x.append(int(face.pos_x))
        msg.y.append(int(face.pos_y))
        msg.size.append(int(face.size))
        msg.conf.append(int(face.conf))
        if face.direction is None:
            msg.LR.append(0)
            msg.UD.append(0)
        else:
            msg.LR.append(int(face.direction.LR))
            msg.UD.append(int(face.direction.UD))
        if face.gaze is None:
            msg.gazeLR.append(0)
            msg.gazeUD.append(0)
        else:
            msg.gazeLR.append(int(face.gaze.gazeLR))
            msg.gazeUD.append(int(face.gaze.gazeUD))

    #顔の大きさによる並び替え
    '''
    if msg.face_count > 0:
        a = zip(msg.id, msg.x, msg.y, msg.size, msg.conf, msg.LR, msg.UD, msg.gazeLR, msg.gazeUD)
        a.sort(key=itemgetter(3))
        msg.id, msg.x, msg.y, msg.size, msg.conf, msg.LR, msg.UD, msg.gazeLR, msg.gazeUD = zip(*a)
    '''

    return msg


def main(nodename="talker", chattername="chatter_okao", portname="/dev/ttyACM0"):
    # ROS追加：配信者の設定
    pub = rospy.Publisher(chattername, face_info, queue_size=5)
    rospy.init_node(nodename, anonymous=True)
    rate = rospy.Rate(500) # 5hz
    # 引数チェック
    
    portinfo = portname
    baudrate = int(9600)
    use_stb = p2def.USE_STB_ON
    #(portinfo, baudrate, use_stb) = _parse_arg(sys.argv)
    connector = SerialConnector()
    hvc_p2_api = HVCP2Api(connector, B5Tdef.exec_func, use_stb)

    # The 1st connection. (It should be 9600 baud.)
    hvc_p2_api.connect(portinfo, 9600, 10)
    _check_connection(hvc_p2_api)
    hvc_p2_api.set_uart_baudrate(baudrate) # Changing to the specified baudrate
    hvc_p2_api.disconnect()

    # The 2nd connection in specified baudrate
    hvc_p2_api.connect(portinfo, baudrate, timeout)
    _check_connection(hvc_p2_api)

    try:
	# Sets HVC-P2 parameters
        _set_hvc_p2_parameters(hvc_p2_api)
       
        # Sets STB library parameters
        _set_stb_parameters(hvc_p2_api)

        # hvc_tracking_result = HVCTrackingResult()
        hvc_tracking_result = HVCTrackingResult() # 追加：ROS

        print(type(hvc_tracking_result))

        img = GrayscaleImage()


        while True:
            start = time.time()
            (res_code, stb_status) = hvc_p2_api.execute(B5Tdef.output_img_type,\
                                                      hvc_tracking_result, img)
            elapsed_time = str(float(time.time() - start) * 1000)[0:6]

            if B5Tdef.output_img_type != p2def.OUT_IMG_TYPE_NONE:
                img.save(img_fname)

            print(("==== Elapsed time:{0}".format(elapsed_time)) + "[msec] ====")

            print(hvc_tracking_result)
            # ROS追加：メッセージ更新
            msg = getMsg(hvc_tracking_result)

            #rospy.loginfo(msg)
            pub.publish(msg)

            #print(hvc_tracking_result)
            
            print("Press Ctrl+C Key to end:\n")

    except KeyboardInterrupt:
        pass

    finally:
        hvc_p2_api.set_uart_baudrate(p2def.DEFAULT_BAUD)
        hvc_p2_api.disconnect()


if __name__ == '__main__':
	args = sys.argv

	# error: Argument is incorrect...
	if len(args) != 4:
		print("error: Argument is incorrect...")
		print("hint: execution.py \"talker\" \"chatter_okao\" \"/dev/ttyACM0\"")

	else:
		nodename = args[1]
		chattername = args[2]
		portname = args[3]

		try:
			main( nodename, chattername, portname )
		except rospy.ROSInterruptException:
			pass
