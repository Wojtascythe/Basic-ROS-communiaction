#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
import sys

class Generator:
    def __init__(self, time_step = 0.5, w=1, a=0):
        self.pub = rospy.Publisher('output', Float64, queue_size=10)
        rospy.init_node('generator', anonymous=True)
        self.time_step = time_step
        self.frec = 1/self.time_step
        self.rate = rospy.Rate(self.frec) # 10hz
        self.t = 0
        self.a = a
        self.w = w

    def generator(self):
        while not rospy.is_shutdown():
            result = math.sin(self.w*self.t+self.a)
            rospy.loginfo(result)
            self.pub.publish(result)
            self.t += self.time_step
            self.rate.sleep()


if __name__ == '__main__':
    try:
        
        print(float(sys.argv[1]))
        if len(sys.argv) > 1:
            generator = Generator(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
        else:
            generator = Generator()
        generator.generator()
    except rospy.ROSInterruptException:
        pass