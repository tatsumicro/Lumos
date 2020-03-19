# -*- coding: utf-8 -*-

import p2def

#-------------------------
# B5T-007001 settings
#-------------------------
# Execute functions
exec_func = p2def.EX_FACE\
          | p2def.EX_DIRECTION\
          | p2def.EX_GAZE\
          #| p2def.EX_HAND\
          #| p2def.EX_EXPRESSION\
           #| p2def.EX_AGE\
           #| p2def.EX_GENDER\
           #| p2def.EX_EXPRESSION\
           #| p2def.EX_RECOGNITION\
           #| p2def.EX_BLINK\
           #| p2def.EX_BODY\

#exec_func = p2def.EX_NONE  # Please use this to get just the image.

# HVC camera angle setting
hvc_camera_angle = p2def.HVC_CAM_ANGLE_0
                       # HVC_CAM_ANGLE_90
                       # HVC_CAM_ANGLE_180
                       # HVC_CAM_ANGLE_270

# Output image type
output_img_type = p2def.OUT_IMG_TYPE_NONE
                      # OUT_IMG_TYPE_QQVGA
                      # OUT_IMG_TYPE_QVGA

# しきい値設定
body_thresh = 500         # Threshold for Human body detection [1 to 1000]
hand_thresh = 500         # Threshold for Hand detection       [1 to 1000]
face_thresh = 500         # Threshold for Face detection       [1 to 1000]
recognition_thresh = 500  # Threshold for Recognition          [0 to 1000]

# 検出サイズ設定
min_body_size = 30      # Mininum human body detection size [20 to 8192]
max_body_size = 8192    # Maximum human body detection size [20 to 8192]
min_hand_size = 40      # Mininum hand detection size       [20 to 8192]
max_hand_size = 8192    # Maximum hand detection size       [20 to 8192]
min_face_size = 64      # Mininum face detection size       [20 to 8192]
max_face_size = 8192    # Maximum face detection size       [20 to 8192]

# Detection face angle settings
face_angle_yaw  = p2def.HVC_FACE_ANGLE_YAW_30
                      # HVC_FACE_ANGLE_YAW_60
                      # HVC_FACE_ANGLE_YAW_90
face_angle_roll = p2def.HVC_FACE_ANGLE_ROLL_15
                      # HVC_FACE_ANGLE_ROLL_45
