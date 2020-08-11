#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
    

class Power:
    def __init__(self):
        pass

    def callback(self, data_input):
        result = data_input.data ** 2
        rospy.loginfo("power " + str(result))
        self.pub.publish(result)

    def power_init(self):
        rospy.init_node('power', anonymous=True)
        self.pub = rospy.Publisher('output', Float64, queue_size=10)
        self.sub = rospy.Subscriber('input', Float64, self.callback)
        rospy.spin()

if __name__ == '__main__':
    try:
        power = Power()
        power.power_init()
    except rospy.ROSInterruptException:
        pass