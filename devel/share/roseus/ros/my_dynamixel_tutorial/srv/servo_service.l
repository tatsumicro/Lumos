;; Auto-generated. Do not edit!


(when (boundp 'my_dynamixel_tutorial::servo_service)
  (if (not (find-package "MY_DYNAMIXEL_TUTORIAL"))
    (make-package "MY_DYNAMIXEL_TUTORIAL"))
  (shadow 'servo_service (find-package "MY_DYNAMIXEL_TUTORIAL")))
(unless (find-package "MY_DYNAMIXEL_TUTORIAL::SERVO_SERVICE")
  (make-package "MY_DYNAMIXEL_TUTORIAL::SERVO_SERVICE"))
(unless (find-package "MY_DYNAMIXEL_TUTORIAL::SERVO_SERVICEREQUEST")
  (make-package "MY_DYNAMIXEL_TUTORIAL::SERVO_SERVICEREQUEST"))
(unless (find-package "MY_DYNAMIXEL_TUTORIAL::SERVO_SERVICERESPONSE")
  (make-package "MY_DYNAMIXEL_TUTORIAL::SERVO_SERVICERESPONSE"))

(in-package "ROS")





(defclass my_dynamixel_tutorial::servo_serviceRequest
  :super ros::object
  :slots (_speed ))

(defmethod my_dynamixel_tutorial::servo_serviceRequest
  (:init
   (&key
    ((:speed __speed) 0.0)
    )
   (send-super :init)
   (setq _speed (float __speed))
   self)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:serialization-length
   ()
   (+
    ;; float64 _speed
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _speed
     (setq _speed (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass my_dynamixel_tutorial::servo_serviceResponse
  :super ros::object
  :slots ())

(defmethod my_dynamixel_tutorial::servo_serviceResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass my_dynamixel_tutorial::servo_service
  :super ros::object
  :slots ())

(setf (get my_dynamixel_tutorial::servo_service :md5sum-) "4641bb0523a3557209606d9bd91ce33a")
(setf (get my_dynamixel_tutorial::servo_service :datatype-) "my_dynamixel_tutorial/servo_service")
(setf (get my_dynamixel_tutorial::servo_service :request) my_dynamixel_tutorial::servo_serviceRequest)
(setf (get my_dynamixel_tutorial::servo_service :response) my_dynamixel_tutorial::servo_serviceResponse)

(defmethod my_dynamixel_tutorial::servo_serviceRequest
  (:response () (instance my_dynamixel_tutorial::servo_serviceResponse :init)))

(setf (get my_dynamixel_tutorial::servo_serviceRequest :md5sum-) "4641bb0523a3557209606d9bd91ce33a")
(setf (get my_dynamixel_tutorial::servo_serviceRequest :datatype-) "my_dynamixel_tutorial/servo_serviceRequest")
(setf (get my_dynamixel_tutorial::servo_serviceRequest :definition-)
      "float64 speed

---
")

(setf (get my_dynamixel_tutorial::servo_serviceResponse :md5sum-) "4641bb0523a3557209606d9bd91ce33a")
(setf (get my_dynamixel_tutorial::servo_serviceResponse :datatype-) "my_dynamixel_tutorial/servo_serviceResponse")
(setf (get my_dynamixel_tutorial::servo_serviceResponse :definition-)
      "float64 speed

---
")



(provide :my_dynamixel_tutorial/servo_service "4641bb0523a3557209606d9bd91ce33a")


