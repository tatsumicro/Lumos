;; Auto-generated. Do not edit!


(when (boundp 'okao::face_info)
  (if (not (find-package "OKAO"))
    (make-package "OKAO"))
  (shadow 'face_info (find-package "OKAO")))
(unless (find-package "OKAO::FACE_INFO")
  (make-package "OKAO::FACE_INFO"))

(in-package "ROS")
;;//! \htmlinclude face_info.msg.html


(defclass okao::face_info
  :super ros::object
  :slots (_face_count _id _x _y _size _conf _LR _UD _gazeLR _gazeUD ))

(defmethod okao::face_info
  (:init
   (&key
    ((:face_count __face_count) 0)
    ((:id __id) (make-array 0 :initial-element 0 :element-type :integer))
    ((:x __x) (make-array 0 :initial-element 0 :element-type :integer))
    ((:y __y) (make-array 0 :initial-element 0 :element-type :integer))
    ((:size __size) (make-array 0 :initial-element 0 :element-type :integer))
    ((:conf __conf) (make-array 0 :initial-element 0 :element-type :integer))
    ((:LR __LR) (make-array 0 :initial-element 0 :element-type :integer))
    ((:UD __UD) (make-array 0 :initial-element 0 :element-type :integer))
    ((:gazeLR __gazeLR) (make-array 0 :initial-element 0 :element-type :integer))
    ((:gazeUD __gazeUD) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _face_count (round __face_count))
   (setq _id __id)
   (setq _x __x)
   (setq _y __y)
   (setq _size __size)
   (setq _conf __conf)
   (setq _LR __LR)
   (setq _UD __UD)
   (setq _gazeLR __gazeLR)
   (setq _gazeUD __gazeUD)
   self)
  (:face_count
   (&optional __face_count)
   (if __face_count (setq _face_count __face_count)) _face_count)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:size
   (&optional __size)
   (if __size (setq _size __size)) _size)
  (:conf
   (&optional __conf)
   (if __conf (setq _conf __conf)) _conf)
  (:LR
   (&optional __LR)
   (if __LR (setq _LR __LR)) _LR)
  (:UD
   (&optional __UD)
   (if __UD (setq _UD __UD)) _UD)
  (:gazeLR
   (&optional __gazeLR)
   (if __gazeLR (setq _gazeLR __gazeLR)) _gazeLR)
  (:gazeUD
   (&optional __gazeUD)
   (if __gazeUD (setq _gazeUD __gazeUD)) _gazeUD)
  (:serialization-length
   ()
   (+
    ;; int32 _face_count
    4
    ;; int32[] _id
    (* 4    (length _id)) 4
    ;; int32[] _x
    (* 4    (length _x)) 4
    ;; int32[] _y
    (* 4    (length _y)) 4
    ;; int32[] _size
    (* 4    (length _size)) 4
    ;; int32[] _conf
    (* 4    (length _conf)) 4
    ;; int32[] _LR
    (* 4    (length _LR)) 4
    ;; int32[] _UD
    (* 4    (length _UD)) 4
    ;; int32[] _gazeLR
    (* 4    (length _gazeLR)) 4
    ;; int32[] _gazeUD
    (* 4    (length _gazeUD)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _face_count
       (write-long _face_count s)
     ;; int32[] _id
     (write-long (length _id) s)
     (dotimes (i (length _id))
       (write-long (elt _id i) s)
       )
     ;; int32[] _x
     (write-long (length _x) s)
     (dotimes (i (length _x))
       (write-long (elt _x i) s)
       )
     ;; int32[] _y
     (write-long (length _y) s)
     (dotimes (i (length _y))
       (write-long (elt _y i) s)
       )
     ;; int32[] _size
     (write-long (length _size) s)
     (dotimes (i (length _size))
       (write-long (elt _size i) s)
       )
     ;; int32[] _conf
     (write-long (length _conf) s)
     (dotimes (i (length _conf))
       (write-long (elt _conf i) s)
       )
     ;; int32[] _LR
     (write-long (length _LR) s)
     (dotimes (i (length _LR))
       (write-long (elt _LR i) s)
       )
     ;; int32[] _UD
     (write-long (length _UD) s)
     (dotimes (i (length _UD))
       (write-long (elt _UD i) s)
       )
     ;; int32[] _gazeLR
     (write-long (length _gazeLR) s)
     (dotimes (i (length _gazeLR))
       (write-long (elt _gazeLR i) s)
       )
     ;; int32[] _gazeUD
     (write-long (length _gazeUD) s)
     (dotimes (i (length _gazeUD))
       (write-long (elt _gazeUD i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _face_count
     (setq _face_count (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32[] _id
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _id (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _id i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _x
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _x (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _x i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _y
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _y (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _y i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _size
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _size (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _size i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _conf
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _conf (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _conf i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _LR
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _LR (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _LR i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _UD
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _UD (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _UD i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _gazeLR
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _gazeLR (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _gazeLR i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32[] _gazeUD
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _gazeUD (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _gazeUD i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get okao::face_info :md5sum-) "67bc21cec1ca544cbc5dca716a0b6dc0")
(setf (get okao::face_info :datatype-) "okao/face_info")
(setf (get okao::face_info :definition-)
      "int32 face_count
int32[] id
int32[] x
int32[] y
int32[] size
int32[] conf
int32[] LR
int32[] UD
int32[] gazeLR
int32[] gazeUD

")



(provide :okao/face_info "67bc21cec1ca544cbc5dca716a0b6dc0")


