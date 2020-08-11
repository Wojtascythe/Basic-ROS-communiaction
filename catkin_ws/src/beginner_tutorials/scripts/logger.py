#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import matplotlib.pyplot as plt

class Logger:
	def __init__(self):
		self.times = []
		self.samples = []


	def callback(self, data):
	    self.samples.append(data.data)
	    self.times.append(len(self.samples))
	    rospy.loginfo("Logger: " + str(data.data))
    	# plt.plot(self.times, self.samples)
    	# plt.draw()
	    # plt.pause(0.0001)
	    # plt.clf()

	    
	def logger_init(self):
	    rospy.init_node('logger', anonymous=True)
	    rospy.Subscriber("input", Float64, self.callback)
	    rospy.spin()

if __name__ == '__main__':
    logger = Logger()
    logger.logger_init()
