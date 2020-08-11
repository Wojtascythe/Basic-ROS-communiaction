#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64


class Sum:
    def __init__(self):
        self.left = None
        self.right = None

    def sum_(self):
        result = self.left + self.right
        rospy.loginfo("sum " + str(result))
        self.pub.publish(result)
        self.left = None
        self.right = None

    def callback1(self, data_input):
        rospy.loginfo("sum left " + str(data_input.data))
        self.left = data_input.data
        if self.right is None:
            return
        self.sum_()
        

    def callback2(self, data_input):
        rospy.loginfo("sum right " + str(data_input.data))
        self.right = data_input.data
        if self.left is None:
            return
        self.sum_()

    def sum_init(self):
        rospy.init_node('summ', anonymous=True)
        self.pub = rospy.Publisher('output', Float64, queue_size=10)
        left_sub = rospy.Subscriber('input1', Float64, self.callback1)
        right_sub = rospy.Subscriber('input2', Float64, self.callback2)
        rospy.spin()

if __name__ == '__main__':
    try:
        su = Sum()
        su.sum_init()
    except rospy.ROSInterruptException:
        pass