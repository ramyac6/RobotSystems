; Auto-generated. Do not edit!


(cl:in-package hiwonder_servo_msgs-msg)


;//! \htmlinclude ActionGroupRunnerResult.msg.html

(cl:defclass <ActionGroupRunnerResult> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (result
    :reader result
    :initarg :result
    :type cl:string
    :initform ""))
)

(cl:defclass ActionGroupRunnerResult (<ActionGroupRunnerResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ActionGroupRunnerResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ActionGroupRunnerResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name hiwonder_servo_msgs-msg:<ActionGroupRunnerResult> is deprecated: use hiwonder_servo_msgs-msg:ActionGroupRunnerResult instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <ActionGroupRunnerResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hiwonder_servo_msgs-msg:name-val is deprecated.  Use hiwonder_servo_msgs-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <ActionGroupRunnerResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader hiwonder_servo_msgs-msg:result-val is deprecated.  Use hiwonder_servo_msgs-msg:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ActionGroupRunnerResult>) ostream)
  "Serializes a message object of type '<ActionGroupRunnerResult>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'result))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'result))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ActionGroupRunnerResult>) istream)
  "Deserializes a message object of type '<ActionGroupRunnerResult>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'result) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'result) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ActionGroupRunnerResult>)))
  "Returns string type for a message object of type '<ActionGroupRunnerResult>"
  "hiwonder_servo_msgs/ActionGroupRunnerResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ActionGroupRunnerResult)))
  "Returns string type for a message object of type 'ActionGroupRunnerResult"
  "hiwonder_servo_msgs/ActionGroupRunnerResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ActionGroupRunnerResult>)))
  "Returns md5sum for a message object of type '<ActionGroupRunnerResult>"
  "bce5bc1805b967315e9937df0cda1034")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ActionGroupRunnerResult)))
  "Returns md5sum for a message object of type 'ActionGroupRunnerResult"
  "bce5bc1805b967315e9937df0cda1034")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ActionGroupRunnerResult>)))
  "Returns full string definition for message of type '<ActionGroupRunnerResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%string name~%string result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ActionGroupRunnerResult)))
  "Returns full string definition for message of type 'ActionGroupRunnerResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%string name~%string result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ActionGroupRunnerResult>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4 (cl:length (cl:slot-value msg 'result))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ActionGroupRunnerResult>))
  "Converts a ROS message object to a list"
  (cl:list 'ActionGroupRunnerResult
    (cl:cons ':name (name msg))
    (cl:cons ':result (result msg))
))
