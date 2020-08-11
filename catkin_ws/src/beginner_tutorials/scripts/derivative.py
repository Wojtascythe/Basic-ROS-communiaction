#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import sys
    
class Derivative:
    def __init__(self, time_step = 0.5):
        self.time_step = time_step
        self.prev = 0

    def callback(self, data_input):
        result = (data_input.data-self.prev)/self.time_step
        self.prev = data_input.data
        rospy.loginfo("derivative " + str(result))
        self.pub.publish(result)

    def derivative_init(self):
        rospy.init_node('derivative', anonymous=True)
        self.pub = rospy.Publisher('output', Float64, queue_size=10)
        self.sub = rospy.Subscriber('input', Float64, self.callback)
        rospy.spin()

if __name__ == '__main__':
    try:
        
        print(float(sys.argv[1]))
        if len(sys.argv) > 1:
            deriv = Derivative(float(sys.argv[1]))
        else:
            deriv = Derivative()
        deriv.derivative_init()
    except rospy.ROSInterruptException:
        pass