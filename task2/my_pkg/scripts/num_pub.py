#!/usr/bin/env python  
import rospy

from my_pkg.msg import two_ints

def callback(data):
    global d,e
    d = data.a
    e = data.b
    rospy.loginfo("The output obtained by multiplication of 4 with the sum of 2 and 3 is %d"% e)
   # publisher()



def listener():
    rospy.init_node('output_listener', anonymous=True)
    rospy.Subscriber("bow_bow", two_ints, callback)


    rospy.spin()



if __name__ == '__main__':
    listener()
