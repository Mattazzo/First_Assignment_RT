#!/usr/bin/env python

# This node is the robot controller which request a target to the server,
# it check robot position and update robot velocity until the target
# is achieved. 
# Then it request for another target.
 
import rospy
import random
import math
import time
from assignment1.srv import Target,TargetResponse
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

## publisher to publish robot velocity
pub_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

## client to request a target 
client = rospy.ServiceProxy('/target',Target)

## distance between robot and target
distance = 1000.0

## target to be achieved
target = Odometry()

## callback function after subscribing for robot position 
# @param pos The position of robot subscribed from world
def positionCallback(pos):
	
	rospy.loginfo("Robot position @[%f,%f]", pos.pose.pose.position.x, pos.pose.pose.position.y)
	
	#calculate distance between robot and target
	distance = math.sqrt(pow(target.pose.pose.position.x - pos.pose.pose.position.x,2) + 
						 pow(target.pose.pose.position.y - pos.pose.pose.position.y,2))
					
	rospy.loginfo("distance: %f", distance)
	
	if(distance > 0.1):
		#target not achieved, set the robot velocity 
		vel = Twist()
		vel.linear.x = (target.pose.pose.position.x - pos.pose.pose.position.x)
		vel.linear.y = (target.pose.pose.position.y - pos.pose.pose.position.y)
		pub_vel.publish(vel)
	else:
		#target achieved, ask for a new target
		response = client(-6.0,6.0)
		target.pose.pose.position.x = response.x
		target.pose.pose.position.y = response.y
		rospy.loginfo("New target @[%f,%f] ", target.pose.pose.position.x,target.pose.pose.position.y)
		
## main function to call target service and subsrcibe for robot position
def main():
	
	#initialize node
	rospy.init_node('robot_controller', anonymous = False)
	
	#calling service
	response = client(-6.0,6.0)
	target.pose.pose.position.x = response.x
	target.pose.pose.position.y = response.y
	
	rospy.loginfo("Received target @[%f,%f]",target.pose.pose.position.x,target.pose.pose.position.y)
	
	#define a subscriber for robot position
	rospy.Subscriber("/odom", Odometry, positionCallback)
	
	rospy.spin()
	
	
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
	
	
	
