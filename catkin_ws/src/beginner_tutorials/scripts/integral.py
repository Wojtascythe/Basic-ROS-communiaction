#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
    
class Integrator:
    def __init__(self, time_step = 0.1):
        self.prev = 0
        self.integral = 0
        self.time_step = time_step

    def callback(self, data_input):
        self.integral += (data_input.data+self.prev)*self.time_step/2
        self.prev = data_input.data
        rospy.loginfo("integral " + str(self.integral))
        self.pub.publish(self.integral)

    def integrator_init(self):
        rospy.init_node('integral', anonymous=True)
        self.pub = rospy.Publisher('output', Float64, queue_size=10)
        self.sub = rospy.Subscriber('input', Float64, self.callback)
        rospy.spin()

if __name__ == '__main__':
    try:
        integrator = Integrator()
        integrator.integrator_init() 
    except rospy.ROSInterruptException:
        pass