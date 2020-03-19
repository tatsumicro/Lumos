
(cl:in-package :asdf)

(defsystem "my_dynamixel_tutorial-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "servo_service" :depends-on ("_package_servo_service"))
    (:file "_package_servo_service" :depends-on ("_package"))
  ))