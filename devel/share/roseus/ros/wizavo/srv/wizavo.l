;; Auto-generated. Do not edit!


(when (boundp 'wizavo::wizavo)
  (if (not (find-package "WIZAVO"))
    (make-package "WIZAVO"))
  (shadow 'wizavo (find-package "WIZAVO")))
(unless (find-package "WIZAVO::WIZAVO")
  (make-package "WIZAVO::WIZAVO"))
(unless (find-package "WIZAVO::WIZAVOREQUEST")
  (make-package "WIZAVO::WIZAVOREQUEST"))
(unless (find-package "WIZAVO::WIZAVORESPONSE")
  (make-package "WIZAVO::WIZAVORESPONSE"))

(in-package "ROS")





(defclass wizavo::wizavoRequest
  :super ros::object
  :slots (_req ))

(defmethod wizavo::wizavoRequest
  (:init
   (&key
    ((:req __req) "")
    )
   (send-super :init)
   (setq _req (string __req))
   self)
  (:req
   (&optional __req)
   (if __req (setq _req __req)) _req)
  (:serialization-length
   ()
   (+
    ;; string _req
    4 (length _req)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _req
       (write-long (length _req) s) (princ _req s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _req
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _req (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass wizavo::wizavoResponse
  :super ros::object
  :slots (_res ))

(defmethod wizavo::wizavoResponse
  (:init
   (&key
    ((:res __res) "")
    )
   (send-super :init)
   (setq _res (string __res))
   self)
  (:res
   (&optional __res)
   (if __res (setq _res __res)) _res)
  (:serialization-length
   ()
   (+
    ;; string _res
    4 (length _res)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _res
       (write-long (length _res) s) (princ _res s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _res
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _res (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass wizavo::wizavo
  :super ros::object
  :slots ())

(setf (get wizavo::wizavo :md5sum-) "fd72814fc41c6bccdf8759d8dea09f77")
(setf (get wizavo::wizavo :datatype-) "wizavo/wizavo")
(setf (get wizavo::wizavo :request) wizavo::wizavoRequest)
(setf (get wizavo::wizavo :response) wizavo::wizavoResponse)

(defmethod wizavo::wizavoRequest
  (:response () (instance wizavo::wizavoResponse :init)))

(setf (get wizavo::wizavoRequest :md5sum-) "fd72814fc41c6bccdf8759d8dea09f77")
(setf (get wizavo::wizavoRequest :datatype-) "wizavo/wizavoRequest")
(setf (get wizavo::wizavoRequest :definition-)
      "string req
---
string res

")

(setf (get wizavo::wizavoResponse :md5sum-) "fd72814fc41c6bccdf8759d8dea09f77")
(setf (get wizavo::wizavoResponse :datatype-) "wizavo/wizavoResponse")
(setf (get wizavo::wizavoResponse :definition-)
      "string req
---
string res

")



(provide :wizavo/wizavo "fd72814fc41c6bccdf8759d8dea09f77")


