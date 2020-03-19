; Auto-generated. Do not edit!


(cl:in-package my_dynamixel_tutorial-msg)


;//! \htmlinclude servo_speed.msg.html

(cl:defclass <servo_speed> (roslisp-msg-protocol:ros-message)
  ((id
    :reader id
    :initarg :id
    :type cl:fixnum
    :initform 0)
   (speed
    :reader speed
    :initarg :speed
    :type cl:float
    :initform 0.0))
)

(cl:defclass servo_speed (<servo_speed>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <servo_speed>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'servo_speed)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name my_dynamixel_tutorial-msg:<servo_speed> is deprecated: use my_dynamixel_tutorial-msg:servo_speed instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <servo_speed>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader my_dynamixel_tutorial-msg:id-val is deprecated.  Use my_dynamixel_tutorial-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <servo_speed>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader my_dynamixel_tutorial-msg:speed-val is deprecated.  Use my_dynamixel_tutorial-msg:speed instead.")
  (speed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <servo_speed>) ostream)
  "Serializes a message object of type '<servo_speed>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id)) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <servo_speed>) istream)
  "Deserializes a message object of type '<servo_speed>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'speed) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<servo_speed>)))
  "Returns string type for a message object of type '<servo_speed>"
  "my_dynamixel_tutorial/servo_speed")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'servo_speed)))
  "Returns string type for a message object of type 'servo_speed"
  "my_dynamixel_tutorial/servo_speed")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<servo_speed>)))
  "Returns md5sum for a message object of type '<servo_speed>"
  "3e1378cae472d979e1a7c8908b73927d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'servo_speed)))
  "Returns md5sum for a message object of type 'servo_speed"
  "3e1378cae472d979e1a7c8908b73927d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<servo_speed>)))
  "Returns full string definition for message of type '<servo_speed>"
  (cl:format cl:nil "uint16 id~%float64 speed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'servo_speed)))
  "Returns full string definition for message of type 'servo_speed"
  (cl:format cl:nil "uint16 id~%float64 speed~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <servo_speed>))
  (cl:+ 0
     2
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <servo_speed>))
  "Converts a ROS message object to a list"
  (cl:list 'servo_speed
    (cl:cons ':id (id msg))
    (cl:cons ':speed (speed msg))
))
