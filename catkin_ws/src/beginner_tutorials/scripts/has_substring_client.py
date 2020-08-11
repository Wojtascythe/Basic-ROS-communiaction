#!/usr/bin/env python

import sys
import rospy
from beginner_tutorials.srv import *

def has_substring_client(string, substring):
    rospy.wait_for_service('has_substring')
    try:
        has_substring = rospy.ServiceProxy('has_substring', Substring)
        resp1 = has_substring(string, substring)
        return resp1.counted
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [string substring]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        string = str(sys.argv[1])
        substring = str(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "Requesting has substring %s in %s"%(substring, string)
    print "Result substring %s in %s = %s"%(substring, string, has_substring_client(string, substring))