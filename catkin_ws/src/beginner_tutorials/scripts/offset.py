#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
    

class Offset:
    def __init__(self, offset=0):
        self.offset = offset

    def callback(self, data_input):
        result = data_input.data + self.offset
        rospy.loginfo("offset " + str(result))
        self.pub.publish(result)

    def offset_init(self):
        rospy.init_node('offset', anonymous=True)
        self.pub = rospy.Publisher('output', Float64, queue_size=10)
        self.sub = rospy.Subscriber('input', Float64, self.callback)
        rospy.spin()

if __name__ == '__main__':
    try:
        offset = Offset()
        offset.offset_init()
    except rospy.ROSInterruptException:
        pass