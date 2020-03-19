;; Auto-generated. Do not edit!


(when (boundp 'srv_test::test)
  (if (not (find-package "SRV_TEST"))
    (make-package "SRV_TEST"))
  (shadow 'test (find-package "SRV_TEST")))
(unless (find-package "SRV_TEST::TEST")
  (make-package "SRV_TEST::TEST"))
(unless (find-package "SRV_TEST::TESTREQUEST")
  (make-package "SRV_TEST::TESTREQUEST"))
(unless (find-package "SRV_TEST::TESTRESPONSE")
  (make-package "SRV_TEST::TESTRESPONSE"))

(in-package "ROS")





(defclass srv_test::testRequest
  :super ros::object
  :slots (_req ))

(defmethod srv_test::testRequest
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

(defclass srv_test::testResponse
  :super ros::object
  :slots (_res ))

(defmethod srv_test::testResponse
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

(defclass srv_test::test
  :super ros::object
  :slots ())

(setf (get srv_test::test :md5sum-) "fd72814fc41c6bccdf8759d8dea09f77")
(setf (get srv_test::test :datatype-) "srv_test/test")
(setf (get srv_test::test :request) srv_test::testRequest)
(setf (get srv_test::test :response) srv_test::testResponse)

(defmethod srv_test::testRequest
  (:response () (instance srv_test::testResponse :init)))

(setf (get srv_test::testRequest :md5sum-) "fd72814fc41c6bccdf8759d8dea09f77")
(setf (get srv_test::testRequest :datatype-) "srv_test/testRequest")
(setf (get srv_test::testRequest :definition-)
      "string req
---
string res

")

(setf (get srv_test::testResponse :md5sum-) "fd72814fc41c6bccdf8759d8dea09f77")
(setf (get srv_test::testResponse :datatype-) "srv_test/testResponse")
(setf (get srv_test::testResponse :definition-)
      "string req
---
string res

")



(provide :srv_test/test "fd72814fc41c6bccdf8759d8dea09f77")


