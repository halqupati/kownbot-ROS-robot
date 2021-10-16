#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO
import time

leftEn = 12	        #	Purple
rightEn = 13		#	Red

w_r=0.0 
w_l=0.0

linear = 0.0
angular = 0.0
#wheel_rad is the wheel radius ,wheel_sep is
wheel_rad = 0.03
wheel_sep = 0.14

leftBackward = 5	#	Blue
leftForward = 6		#	Green
rightForward = 16	#	Yellow
rightBackward = 20	#	Orange

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(leftEn, GPIO.OUT)
GPIO.setup(rightEn, GPIO.OUT)
GPIO.setup(leftForward, GPIO.OUT)
GPIO.setup(leftBackward, GPIO.OUT)
GPIO.setup(rightForward, GPIO.OUT)
GPIO.setup(rightBackward, GPIO.OUT)

pwmL = GPIO.PWM(leftEn, 20)
pwmL.start(0)
pwmR = GPIO.PWM(rightEn, 20)
pwmR.start(0)
 
def rmotor(Pulse_Width1):
    print('Right')    
    if (Pulse_Width1 > 0){
         print('going forward')
         pwmR.ChangeDutyCycle(10)
         GPIO.output(rightForward, GPIO.HIGH)
         GPIO.output(rightBackward, GPIO.LOW);
         }
    elif (Pulse_Width1 < 0){
         print('going backward')
         pwmR.ChangeDutyCycle(10)
         GPIO.output(rightForward, GPIO.LOW)
         GPIO.output(rightBackward, GPIO.HIGH)
         }
    else (Pulse_Width1 == 0){
         print('stopping')
         pwmR.ChangeDutyCycle(0)
         GPIO.output(rightForward, GPIO.LOW)
         GPIO.output(rightBackward, GPIO.LOW)
         }
         
def lmotor(Pulse_Width1):
    print('Left motor ') 
    if (Pulse_Width1 > 0){
         print('going forward')
         pwmR.ChangeDutyCycle(10)
         GPIO.output(leftForward, GPIO.HIGH)
         GPIO.output(leftBackward, GPIO.LOW);
         }
    elif (Pulse_Width1 < 0){
         print('going backward')
         pwmR.ChangeDutyCycle(10)
         GPIO.output(leftForward, GPIO.LOW)
         GPIO.output(leftBackward, GPIO.HIGH)
         }
    else (Pulse_Width1 == 0){
         print('stopping')
         pwmR.ChangeDutyCycle(0)
         GPIO.output(leftForward, GPIO.LOW)
         GPIO.output(leftBackward, GPIO.LOW)
         }

def callback(data):
    linear = data.linear.x
    angular = data.angular.z

    w_r = (linear/wheel_rad) + ((angular*wheel_sep)/(2.0*wheel_rad));
    w_l = (linear/wheel_rad) - ((angular*wheel_sep)/(2.0*wheel_rad));
    print(str(w_r)+"\t"+str(w_l))

        
def listener():
    rospy.init_node('cmdvel_listener', anonymous=False)
    rospy.Subscriber("/cmd_vel", Twist, callback)
    rospy.spin()

if __name__== '__main__':
    print('AISCBOT Differential Drive Initialized')
    listener()
    rmotor(w_r*10)
    lmotor(w_l*10)
