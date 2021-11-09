README for Junior Clinic - Robotic Arm - Finger and Arm Servo Control

Author: Kyle Rettig  
Created: November 9, 2021
Latest Update: Initial Commit

Description: Uses I2C to control up to 16 servos which contribute to moving a robotic hand
________________________________________________________________________________________________________________________________________  
FILES REQUIRED:  
 + ServoKit from https://circuitpython.readthedocs.io/projects/servokit/en/latest/
 + time
 + GPIO from https://github.com/NVIDIA/jetson-gpio
 + board
 + busio
________________________________________________________________________________________________________________________________________  
VARIABLES USED:  
 + fingers  
 + hand  
________________________________________________________________________________________________________________________________________  
PROGRAM FUNCTIONS:  
 * Close Hand
 * Open Hand
 * Single Finger Extended
________________________________________________________________________________________________________________________________________  
Requires use of PWM Servo Motor Driver IIC Module https://www.amazon.com/dp/B07H9ZTWNC/ref=cm_sw_r_cp_api_glc_fabc_SZTN5ZM4QEHS9NZQFS9B
As well as Jetson Nano 2GB

HandConfigurations.py is configured to initialize the I2C header and configure hand signals based on user input. This is planned to be changed to make use of the MyoBand to use electrical signals from an arm to control a robotic arm


