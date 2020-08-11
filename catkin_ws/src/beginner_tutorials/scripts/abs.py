#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
    


class Abs:
    def __init__(self):
        pass

    def callback(self, data_input):
        result = abs(data_input.data)
        rospy.loginfo("abs " + str(result))
        self.pub.publish(result)

    def abs_init(self):
        rospy.init_node('abs', anonymous=True)
        self.pub = rospy.Publisher('output', Float64, queue_size=10)
        self.sub = rospy.Subscriber('input', Float64, self.callback)
        rospy.spin()

if __name__ == '__main__':
    try:
        abs = Abs()
        abs.abs_init()
    except rospy.ROSInterruptException:
        pass