#!/usr/bin/env python
 
# This node is the server which provide a target for the robot 

import rospy
import random
from assignment1.srv import Target,TargetResponse	
	
## Server function to give a target for robot 
# @param request The minimum and the maximum coordinate for a target
# @return response The target for robot
def targetCallback(request):
	
	#Target for robot
	response = TargetResponse();
	response.x = random.uniform(request.minimum,request.maximum)
	response.y = random.uniform(request.minimum,request.maximum)

	rospy.loginfo("Target @[%f,%f]", response.x, response.y)
	
	return response
	
## Main function to execute the service 
def main():
	
	#node initialization
	rospy.init_node('target_server', anonymous = False)
	
	rospy.loginfo("Server ready to give a target\n")
	
	#call  Target service
	srv = rospy.Service("/target",Target,targetCallback)
	
	rospy.spin()
	
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
	
   
