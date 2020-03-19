; Auto-generated. Do not edit!


(cl:in-package wizavo-srv)


;//! \htmlinclude wizavo-request.msg.html

(cl:defclass <wizavo-request> (roslisp-msg-protocol:ros-message)
  ((req
    :reader req
    :initarg :req
    :type cl:string
    :initform ""))
)

(cl:defclass wizavo-request (<wizavo-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wizavo-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wizavo-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name wizavo-srv:<wizavo-request> is deprecated: use wizavo-srv:wizavo-request instead.")))

(cl:ensure-generic-function 'req-val :lambda-list '(m))
(cl:defmethod req-val ((m <wizavo-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader wizavo-srv:req-val is deprecated.  Use wizavo-srv:req instead.")
  (req m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wizavo-request>) ostream)
  "Serializes a message object of type '<wizavo-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'req))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'req))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wizavo-request>) istream)
  "Deserializes a message object of type '<wizavo-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'req) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'req) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wizavo-request>)))
  "Returns string type for a service object of type '<wizavo-request>"
  "wizavo/wizavoRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wizavo-request)))
  "Returns string type for a service object of type 'wizavo-request"
  "wizavo/wizavoRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wizavo-request>)))
  "Returns md5sum for a message object of type '<wizavo-request>"
  "fd72814fc41c6bccdf8759d8dea09f77")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wizavo-request)))
  "Returns md5sum for a message object of type 'wizavo-request"
  "fd72814fc41c6bccdf8759d8dea09f77")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wizavo-request>)))
  "Returns full string definition for message of type '<wizavo-request>"
  (cl:format cl:nil "string req~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wizavo-request)))
  "Returns full string definition for message of type 'wizavo-request"
  (cl:format cl:nil "string req~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wizavo-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'req))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wizavo-request>))
  "Converts a ROS message object to a list"
  (cl:list 'wizavo-request
    (cl:cons ':req (req msg))
))
;//! \htmlinclude wizavo-response.msg.html

(cl:defclass <wizavo-response> (roslisp-msg-protocol:ros-message)
  ((res
    :reader res
    :initarg :res
    :type cl:string
    :initform ""))
)

(cl:defclass wizavo-response (<wizavo-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wizavo-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wizavo-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name wizavo-srv:<wizavo-response> is deprecated: use wizavo-srv:wizavo-response instead.")))

(cl:ensure-generic-function 'res-val :lambda-list '(m))
(cl:defmethod res-val ((m <wizavo-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader wizavo-srv:res-val is deprecated.  Use wizavo-srv:res instead.")
  (res m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wizavo-response>) ostream)
  "Serializes a message object of type '<wizavo-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'res))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'res))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wizavo-response>) istream)
  "Deserializes a message object of type '<wizavo-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'res) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'res) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wizavo-response>)))
  "Returns string type for a service object of type '<wizavo-response>"
  "wizavo/wizavoResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wizavo-response)))
  "Returns string type for a service object of type 'wizavo-response"
  "wizavo/wizavoResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wizavo-response>)))
  "Returns md5sum for a message object of type '<wizavo-response>"
  "fd72814fc41c6bccdf8759d8dea09f77")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wizavo-response)))
  "Returns md5sum for a message object of type 'wizavo-response"
  "fd72814fc41c6bccdf8759d8dea09f77")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wizavo-response>)))
  "Returns full string definition for message of type '<wizavo-response>"
  (cl:format cl:nil "string res~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wizavo-response)))
  "Returns full string definition for message of type 'wizavo-response"
  (cl:format cl:nil "string res~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wizavo-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'res))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wizavo-response>))
  "Converts a ROS message object to a list"
  (cl:list 'wizavo-response
    (cl:cons ':res (res msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'wizavo)))
  'wizavo-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'wizavo)))
  'wizavo-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wizavo)))
  "Returns string type for a service object of type '<wizavo>"
  "wizavo/wizavo")