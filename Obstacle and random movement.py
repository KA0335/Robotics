#!/usr/bin/env python
import rospy 
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist 
import random

class t3():
    def __init__(self):
        self.move = Twist() 
        rospy.init_node('random_walk')
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)  
        self.sub = rospy.Subscriber("/scan", LaserScan, self.callback)  
        self.tStart = rospy.Time.now().to_sec()
        self.reset = False
        rospy.spin() 

    def callback(self,dt): 
        thr1 = 0.5 
        speed = 0.2
        if dt.ranges[0]>thr1 and dt.ranges[25]>thr1 and dt.ranges[335]>thr1:
            self.move=self.randomM(speed,self.tStart,self.move) 
        else:
            self.move.linear.x = 0.0 
            self.move.angular.z = 0.5 
            self.tStart= rospy.Time.now().to_sec()
        self.pub.publish(self.move) 

    def randomM(self,speed,tStart,move):
        tEnd = rospy.Time.now().to_sec()
        theta= random.uniform(-0.5,0.5)
        d= speed*(tEnd-tStart)
        print(tStart,tEnd,d)
        if d>3:
            move.linear.x = 0.0
            move.angular.z = theta
            self.tStart= rospy.Time.now().to_sec()
            self.reset = True
        elif self.reset:
            if tEnd-self.tStart > 2:
                self.reset=False
                self.tStart= rospy.Time.now().to_sec()
        else:
            move.linear.x = 0.2
            move.angular.z = 0.0
        return move

if __name__ == '__main__':
    t3()