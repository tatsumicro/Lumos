
(cl:in-package :asdf)

(defsystem "okao-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "face_info" :depends-on ("_package_face_info"))
    (:file "_package_face_info" :depends-on ("_package"))
  ))