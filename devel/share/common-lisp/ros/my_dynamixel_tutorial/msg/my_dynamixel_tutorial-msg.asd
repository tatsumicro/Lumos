
(cl:in-package :asdf)

(defsystem "my_dynamixel_tutorial-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "servo_rad" :depends-on ("_package_servo_rad"))
    (:file "_package_servo_rad" :depends-on ("_package"))
    (:file "servo_speed" :depends-on ("_package_servo_speed"))
    (:file "_package_servo_speed" :depends-on ("_package"))
  ))