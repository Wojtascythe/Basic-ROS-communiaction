#!/usr/bin/env python
# license removed for brevity
import rospy
from beginner_tutorials.msg import DateTime
import datetime

months = ["stycznia", "lutego", "marca", "kwietnia", "maja", "czerwca", "lipca",
            "sierpnia", "wrzesnia", "pazdziernika", "listopada", "grudnia"]

def date_time_talker():
    pub = rospy.Publisher('clock', DateTime, queue_size=10)
    rospy.init_node('date_time_talker', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        now = datetime.datetime.now()
        #print now.year, now.month, now.day, now.hour, now.minute, now.second
        date_time = DateTime()
        date_time.year = now.year
        date_time.month = months[now.month-1]
        date_time.day = now.day
        date_time.hour = now.hour
        date_time.minute = now.minute
        date_time.seconds = now.second
        rospy.loginfo(date_time)
        pub.publish(date_time)
        rate.sleep()

if __name__ == '__main__':
    try:
        date_time_talker()
    except rospy.ROSInterruptException:
        pass