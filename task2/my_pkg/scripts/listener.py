#!/usr/bin/env python
import rospy
from my_pkg.msg import two_ints

d =None
e =None
def callback(data):
    global d,e
    d = data.a
    e = data.b
   # rospy.loginfo("%d is number 1 is :  the number 2 is%d" % (data.a,data.b))
    publisher()



def print_custom():
    c = d+e
    f = c*4
    return c, f

def publisher():
    pub = rospy.Publisher("bow_bow", two_ints, queue_size=1)
    x,y = print_custom()
    r=rospy.Rate(1)
    msg = two_ints()
    while not rospy.is_shutdown():
      msg.a = x
      msg.b = y
      pub.publish(msg)
      #rospy.loginfo("The output obtained by multiplication of 4 with the sum of 2 and 3 is %d"% y)
      r.sleep()
     
 
   
def listener():
    rospy.init_node('custom_listener', anonymous=True)
    rospy.Subscriber("tow_ints", two_ints, callback)


    rospy.spin()



if __name__ == '__main__':
    listener()
