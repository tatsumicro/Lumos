;; Auto-generated. Do not edit!


(when (boundp 'my_dynamixel_tutorial::servo_rad)
  (if (not (find-package "MY_DYNAMIXEL_TUTORIAL"))
    (make-package "MY_DYNAMIXEL_TUTORIAL"))
  (shadow 'servo_rad (find-package "MY_DYNAMIXEL_TUTORIAL")))
(unless (find-package "MY_DYNAMIXEL_TUTORIAL::SERVO_RAD")
  (make-package "MY_DYNAMIXEL_TUTORIAL::SERVO_RAD"))

(in-package "ROS")
;;//! \htmlinclude servo_rad.msg.html


(defclass my_dynamixel_tutorial::servo_rad
  :super ros::object
  :slots (_id _rad ))

(defmethod my_dynamixel_tutorial::servo_rad
  (:init
   (&key
    ((:id __id) 0)
    ((:rad __rad) 0.0)
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _rad (float __rad))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:rad
   (&optional __rad)
   (if __rad (setq _rad __rad)) _rad)
  (:serialization-length
   ()
   (+
    ;; uint16 _id
    2
    ;; float64 _rad
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint16 _id
       (write-word _id s)
     ;; float64 _rad
       (sys::poke _rad (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint16 _id
     (setq _id (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; float64 _rad
     (setq _rad (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get my_dynamixel_tutorial::servo_rad :md5sum-) "7fcd47675421d9290eb38e0a90977cd6")
(setf (get my_dynamixel_tutorial::servo_rad :datatype-) "my_dynamixel_tutorial/servo_rad")
(setf (get my_dynamixel_tutorial::servo_rad :definition-)
      "uint16 id
float64 rad

")



(provide :my_dynamixel_tutorial/servo_rad "7fcd47675421d9290eb38e0a90977cd6")


