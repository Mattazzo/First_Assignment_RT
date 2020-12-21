# Research Track I - first assignment
#Matteo Azzini 4475165

The assignment requires controlling a holonomic robot in a 2d space with a simple 2d simulator, Stage. 
The simulator can be launched by executing the command:

```
rosrun stage_ros stageros $(rospack find assignment1)/world/exercise.world
```

Then the nodes can be executed, in this order, with the following commands:

```
rosrun assignment1 target_server.py
```
```
rosrun assignment1 robot_controller.py
```

### Content of the package
- docs   		: It's a folder containing online and offline documentation about this package 
- scripts		: It's a folder containing two Python executable, which are the two ROS nodes
- srv    		: It's a folder containing a file in srv exetension to define the service used by nodes
- world  		: It's a folder that define the 2d simulator
- rosgraph.png	: It's an image which graphically represent how nodes comuincate and which topics they use
- CMakeList.txt : It's a file with informations about the compilation  
- package.xml	: It's a file with informations about the compilation


### About ROS nodes and their comunication
- There are two nodes:
		
		- target_server.py	 : -It's a server which, using the service Target, gives back the coordinates of 
								the point to be achieved by the robot
							
		- robot_controller.py: -It's the node which check robot position subsrcibing the topic /odom, that 
							    is published by the 2d simulator 
							    
							   -Then it evaluates the distance between itself and the target to be achieved
							    
							   -If distance is less than 0.1 the robot requests a new target to the 
							    target_server.py, else it sets robot velocity publishing on topic /cmd_vel 
							    to reach the goal point
							    
							   -The 2d simulator subscribe /cmd_vel topic, so the robot moves on the plane
							    and you can see it reaching a target and then go to another target
							    
- chek the file rosgraph.png to see graphically how the nodes comunicate and which topics are used


### Custom messages or services used
-No custom messages are used

-Just one custom service is used:

		-Target.srv: stored in srv folder, it requires two float number(minimum,maximum) as request and 
			     gives back two float numbers(x,y) as response.
			     Minimum and maximum represent the the extremity of the range in which x and y are 
			     randomly choosen
					 
