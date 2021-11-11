import rospy
from sensor_msgs.msg import LaserScan 
from geometry_msgs.msg import Twist 

def callback(dt):
    thr1 = 0.2 
    if dt.ranges[250]>thr1 and dt.ranges[300]>thr1:
        if dt.ranges[250]> dt.ranges[300]:
            move.linear.x = 0 
            move.angular.z = 0.5 
        elif dt.ranges[300] - dt.ranges[250]> 0.1:
            move.linear.x = 0.0 
            move.angular.z = -0.5 
        else: 
            move.linear.x = 0.2
            move.angular.z = 0.0
    else:
        move.linear.x = 0.2
        move.angular.z = 0.2

    pub.publish(move) 


move = Twist() 
rospy.init_node('wall_follow') 
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)  
sub = rospy.Subscriber("/scan", LaserScan, callback)  
rospy.spin()