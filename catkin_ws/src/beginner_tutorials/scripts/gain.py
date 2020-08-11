#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import sys
    
class Gain:
    def __init__(self, k=1):
        self.k = k

    def callback(self, data_input):
        result = data_input.data * self.k
        rospy.loginfo("gain " + str(result))
        self.pub.publish(result)

    def gain_init(self):
        rospy.init_node('gain', anonymous=True)
        self.pub = rospy.Publisher('output', Float64, queue_size=10)
        self.sub = rospy.Subscriber('input', Float64, self.callback)
        rospy.spin()

if __name__ == '__main__':
    try:
        print(float(sys.argv[1]))
        if len(sys.argv) > 1:
            gain = Gain(float(sys.argv[1]))
        else:
            gain = Gain()
        gain.gain_init()
    except rospy.ROSInterruptException:
        pass