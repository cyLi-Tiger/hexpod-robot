#Import everything in the control module, 
#including functions, classes, variables, and more.
from Control import *
from Ultrasonic import *
from IMU import *
from Servo import *
import numpy as np

#Creating object 'control' of 'Control' class.
c=Control()
sonic=Ultrasonic()
s1=Servo()

#example:
#data=['CMD_MOVE', '1', '0', '25', '10', '0']
#Move command:'CMD_MOVE'
#Gait Mode: "1"
#Moving direction: x='0',y='25'
#Delay:'10'
#Action Mode : '0'   Angleless turn 

#0 is the right of the robot, 180 is the left
def move_dir(des_vel, des_ang):
    x=des_vel*np.cos(np.pi-des_ang)
    y=des_vel*np.sin(np.pi-des_ang)
    data=['CMD_MOVE', '1', str(x), str(y), '10', '0']
    for i in range(3):
        c.run(data)

def move_forward():
    data=['CMD_MOVE', '1', '0', '35', '10', '0']
    for i in range(3):
        c.run(data)



if __name__=='main':
    while True:
        if sonic.getDistance()<0.2:
            for i in range(12):
                s1.setServoAngle(60+i*5)
                if sonic.getDistance()>0.5:
                    s1.setServoAngle(90)
                    move_dir(40, 60+i*5)
                    break
        move_forward()

