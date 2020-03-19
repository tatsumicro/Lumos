;; Auto-generated. Do not edit!


(when (boundp 'my_dynamixel_tutorial::servo_speed)
  (if (not (find-package "MY_DYNAMIXEL_TUTORIAL"))
    (make-package "MY_DYNAMIXEL_TUTORIAL"))
  (shadow 'servo_speed (find-package "MY_DYNAMIXEL_TUTORIAL")))
(unless (find-package "MY_DYNAMIXEL_TUTORIAL::SERVO_SPEED")
  (make-package "MY_DYNAMIXEL_TUTORIAL::SERVO_SPEED"))

(in-package "ROS")
;;//! \htmlinclude servo_speed.msg.html


(defclass my_dynamixel_tutorial::servo_speed
  :super ros::object
  :slots (_id _speed ))

(defmethod my_dynamixel_tutorial::servo_speed
  (:init
   (&key
    ((:id __id) 0)
    ((:speed __speed) 0.0)
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _speed (float __speed))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:serialization-length
   ()
   (+
    ;; uint16 _id
    2
    ;; float64 _speed
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _id
       (write-word _id s)
     ;; float64 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _id
     (setq _id (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; float64 _speed
     (setq _speed (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get my_dynamixel_tutorial::servo_speed :md5sum-) "3e1378cae472d979e1a7c8908b73927d")
(setf (get my_dynamixel_tutorial::servo_speed :datatype-) "my_dynamixel_tutorial/servo_speed")
(setf (get my_dynamixel_tutorial::servo_speed :definition-)
      "uint16 id
float64 speed

")



(provide :my_dynamixel_tutorial/servo_speed "3e1378cae472d979e1a7c8908b73927d")


