
(cl:in-package :asdf)

(defsystem "wizavo-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "wizavo" :depends-on ("_package_wizavo"))
    (:file "_package_wizavo" :depends-on ("_package"))
  ))