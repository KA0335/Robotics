#!/usr/bin/env python
import rospy 
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist 

def callback(dt): 
    thr1 = 0.5 
    if dt.ranges[0]>thr1 and dt.ranges[25]>thr1 and dt.ranges[335]>thr1:
        move.linear.x = 0.2 
        move.angular.z = 0.0 
    else:
        move.linear.x = 0.0 
        move.angular.z = 0.5 
    pub.publish(move) 

move = Twist() 
rospy.init_node('obstacle_avoider')
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)  
sub = rospy.Subscriber("/scan", LaserScan, callback)  
rospy.spin()