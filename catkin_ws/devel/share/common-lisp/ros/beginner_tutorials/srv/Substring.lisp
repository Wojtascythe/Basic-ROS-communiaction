; Auto-generated. Do not edit!


(cl:in-package beginner_tutorials-srv)


;//! \htmlinclude Substring-request.msg.html

(cl:defclass <Substring-request> (roslisp-msg-protocol:ros-message)
  ((message
    :reader message
    :initarg :message
    :type cl:string
    :initform "")
   (substring
    :reader substring
    :initarg :substring
    :type cl:string
    :initform ""))
)

(cl:defclass Substring-request (<Substring-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Substring-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Substring-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name beginner_tutorials-srv:<Substring-request> is deprecated: use beginner_tutorials-srv:Substring-request instead.")))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <Substring-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-srv:message-val is deprecated.  Use beginner_tutorials-srv:message instead.")
  (message m))

(cl:ensure-generic-function 'substring-val :lambda-list '(m))
(cl:defmethod substring-val ((m <Substring-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-srv:substring-val is deprecated.  Use beginner_tutorials-srv:substring instead.")
  (substring m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Substring-request>) ostream)
  "Serializes a message object of type '<Substring-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'substring))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'substring))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Substring-request>) istream)
  "Deserializes a message object of type '<Substring-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'substring) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'substring) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Substring-request>)))
  "Returns string type for a service object of type '<Substring-request>"
  "beginner_tutorials/SubstringRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Substring-request)))
  "Returns string type for a service object of type 'Substring-request"
  "beginner_tutorials/SubstringRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Substring-request>)))
  "Returns md5sum for a message object of type '<Substring-request>"
  "7129f2c6cda31fb0fb8a596e2efc394a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Substring-request)))
  "Returns md5sum for a message object of type 'Substring-request"
  "7129f2c6cda31fb0fb8a596e2efc394a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Substring-request>)))
  "Returns full string definition for message of type '<Substring-request>"
  (cl:format cl:nil "string message~%string substring~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Substring-request)))
  "Returns full string definition for message of type 'Substring-request"
  (cl:format cl:nil "string message~%string substring~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Substring-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'message))
     4 (cl:length (cl:slot-value msg 'substring))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Substring-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Substring-request
    (cl:cons ':message (message msg))
    (cl:cons ':substring (substring msg))
))
;//! \htmlinclude Substring-response.msg.html

(cl:defclass <Substring-response> (roslisp-msg-protocol:ros-message)
  ((counted
    :reader counted
    :initarg :counted
    :type cl:integer
    :initform 0))
)

(cl:defclass Substring-response (<Substring-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Substring-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Substring-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name beginner_tutorials-srv:<Substring-response> is deprecated: use beginner_tutorials-srv:Substring-response instead.")))

(cl:ensure-generic-function 'counted-val :lambda-list '(m))
(cl:defmethod counted-val ((m <Substring-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader beginner_tutorials-srv:counted-val is deprecated.  Use beginner_tutorials-srv:counted instead.")
  (counted m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Substring-response>) ostream)
  "Serializes a message object of type '<Substring-response>"
  (cl:let* ((signed (cl:slot-value msg 'counted)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Substring-response>) istream)
  "Deserializes a message object of type '<Substring-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'counted) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Substring-response>)))
  "Returns string type for a service object of type '<Substring-response>"
  "beginner_tutorials/SubstringResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Substring-response)))
  "Returns string type for a service object of type 'Substring-response"
  "beginner_tutorials/SubstringResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Substring-response>)))
  "Returns md5sum for a message object of type '<Substring-response>"
  "7129f2c6cda31fb0fb8a596e2efc394a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Substring-response)))
  "Returns md5sum for a message object of type 'Substring-response"
  "7129f2c6cda31fb0fb8a596e2efc394a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Substring-response>)))
  "Returns full string definition for message of type '<Substring-response>"
  (cl:format cl:nil "int64 counted~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Substring-response)))
  "Returns full string definition for message of type 'Substring-response"
  (cl:format cl:nil "int64 counted~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Substring-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Substring-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Substring-response
    (cl:cons ':counted (counted msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Substring)))
  'Substring-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Substring)))
  'Substring-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Substring)))
  "Returns string type for a service object of type '<Substring>"
  "beginner_tutorials/Substring")