; Auto-generated. Do not edit!


(cl:in-package my_dynamixel_tutorial-srv)


;//! \htmlinclude servo_service-request.msg.html

(cl:defclass <servo_service-request> (roslisp-msg-protocol:ros-message)
  ((speed
    :reader speed
    :initarg :speed
    :type cl:float
    :initform 0.0))
)

(cl:defclass servo_service-request (<servo_service-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <servo_service-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'servo_service-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name my_dynamixel_tutorial-srv:<servo_service-request> is deprecated: use my_dynamixel_tutorial-srv:servo_service-request instead.")))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <servo_service-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader my_dynamixel_tutorial-srv:speed-val is deprecated.  Use my_dynamixel_tutorial-srv:speed instead.")
  (speed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <servo_service-request>) ostream)
  "Serializes a message object of type '<servo_service-request>"
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <servo_service-request>) istream)
  "Deserializes a message object of type '<servo_service-request>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<servo_service-request>)))
  "Returns string type for a service object of type '<servo_service-request>"
  "my_dynamixel_tutorial/servo_serviceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'servo_service-request)))
  "Returns string type for a service object of type 'servo_service-request"
  "my_dynamixel_tutorial/servo_serviceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<servo_service-request>)))
  "Returns md5sum for a message object of type '<servo_service-request>"
  "4641bb0523a3557209606d9bd91ce33a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'servo_service-request)))
  "Returns md5sum for a message object of type 'servo_service-request"
  "4641bb0523a3557209606d9bd91ce33a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<servo_service-request>)))
  "Returns full string definition for message of type '<servo_service-request>"
  (cl:format cl:nil "float64 speed~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'servo_service-request)))
  "Returns full string definition for message of type 'servo_service-request"
  (cl:format cl:nil "float64 speed~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <servo_service-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <servo_service-request>))
  "Converts a ROS message object to a list"
  (cl:list 'servo_service-request
    (cl:cons ':speed (speed msg))
))
;//! \htmlinclude servo_service-response.msg.html

(cl:defclass <servo_service-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass servo_service-response (<servo_service-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <servo_service-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'servo_service-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name my_dynamixel_tutorial-srv:<servo_service-response> is deprecated: use my_dynamixel_tutorial-srv:servo_service-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <servo_service-response>) ostream)
  "Serializes a message object of type '<servo_service-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <servo_service-response>) istream)
  "Deserializes a message object of type '<servo_service-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<servo_service-response>)))
  "Returns string type for a service object of type '<servo_service-response>"
  "my_dynamixel_tutorial/servo_serviceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'servo_service-response)))
  "Returns string type for a service object of type 'servo_service-response"
  "my_dynamixel_tutorial/servo_serviceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<servo_service-response>)))
  "Returns md5sum for a message object of type '<servo_service-response>"
  "4641bb0523a3557209606d9bd91ce33a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'servo_service-response)))
  "Returns md5sum for a message object of type 'servo_service-response"
  "4641bb0523a3557209606d9bd91ce33a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<servo_service-response>)))
  "Returns full string definition for message of type '<servo_service-response>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'servo_service-response)))
  "Returns full string definition for message of type 'servo_service-response"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <servo_service-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <servo_service-response>))
  "Converts a ROS message object to a list"
  (cl:list 'servo_service-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'servo_service)))
  'servo_service-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'servo_service)))
  'servo_service-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'servo_service)))
  "Returns string type for a service object of type '<servo_service>"
  "my_dynamixel_tutorial/servo_service")