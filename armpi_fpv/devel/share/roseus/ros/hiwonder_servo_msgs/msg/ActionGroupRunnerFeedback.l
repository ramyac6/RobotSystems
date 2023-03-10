;; Auto-generated. Do not edit!


(when (boundp 'hiwonder_servo_msgs::ActionGroupRunnerFeedback)
  (if (not (find-package "HIWONDER_SERVO_MSGS"))
    (make-package "HIWONDER_SERVO_MSGS"))
  (shadow 'ActionGroupRunnerFeedback (find-package "HIWONDER_SERVO_MSGS")))
(unless (find-package "HIWONDER_SERVO_MSGS::ACTIONGROUPRUNNERFEEDBACK")
  (make-package "HIWONDER_SERVO_MSGS::ACTIONGROUPRUNNERFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude ActionGroupRunnerFeedback.msg.html


(defclass hiwonder_servo_msgs::ActionGroupRunnerFeedback
  :super ros::object
  :slots (_name _step ))

(defmethod hiwonder_servo_msgs::ActionGroupRunnerFeedback
  (:init
   (&key
    ((:name __name) "")
    ((:step __step) 0)
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _step (round __step))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:step
   (&optional __step)
   (if __step (setq _step __step)) _step)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; uint32 _step
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; uint32 _step
       (write-long _step s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; uint32 _step
     (setq _step (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get hiwonder_servo_msgs::ActionGroupRunnerFeedback :md5sum-) "be888268ba53e256c1e062ac34ecaafc")
(setf (get hiwonder_servo_msgs::ActionGroupRunnerFeedback :datatype-) "hiwonder_servo_msgs/ActionGroupRunnerFeedback")
(setf (get hiwonder_servo_msgs::ActionGroupRunnerFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
string name
uint32 step

")



(provide :hiwonder_servo_msgs/ActionGroupRunnerFeedback "be888268ba53e256c1e062ac34ecaafc")


