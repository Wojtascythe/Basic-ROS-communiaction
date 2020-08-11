#!/usr/bin/env python

from beginner_tutorials.srv import Substring,SubstringResponse
import rospy

def handle_has_substring(req):

    print "Returning has substring '%s' in '%s': %s times"%(req.substring, req.message, req.message.count(req.substring))
    return SubstringResponse(req.message.count(req.substring))

def has_substring_server():
    rospy.init_node('has_substring_server')
    s = rospy.Service('has_substring', Substring, handle_has_substring)
    print "Ready to count substring in message."
    rospy.spin()

if __name__ == "__main__":
    has_substring_server()