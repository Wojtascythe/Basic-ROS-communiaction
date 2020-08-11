#!/usr/bin/env python
import rospy
from beginner_tutorials.msg import DateTime

def callback(data):
    rospy.loginfo("Jest %s %s %s %s:%s:%s", data.day, data.month, data.year, data.hour, data.minute, data.seconds)
    
def date_time_listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('date_time_listener', anonymous=True)

    rospy.Subscriber("clock", DateTime, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    date_time_listener()
