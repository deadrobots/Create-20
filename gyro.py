#!/usr/bin/python
from wallaby import *
import constants as c
import utilities as u
import drive as d

bias = 0

def calibrate_gyro():
    print("we do be calibrating")
    i = 0
    avg = 0
    for i in range(1, 100):
        avg = avg + gyro_x() #help (why not?)
        msleep(1)
        i += 1
    global bias
    bias = avg/i
    print("Bias = ", bias)

def get_theta():
    theta =  0
    theta = theta + abs(gyro_x() - bias) * 10

def turn_by_degrees(left_speed, right_speed, target_theta_deg): #give in degrees
    #calibrate_gyro()
    target_theta_deg = round(target_theta_deg * c.turn_conversion)
    theta = 0
    while(theta < target_theta_deg):
        create_drive_direct(left_speed, right_speed)
        msleep(10)
        theta = get_theta()
    create_drive_direct(0,0)

def drive_straight_simple(speed, time):
    startTime = seconds()
    theta = 0
    while(seconds() - startTime < time):
        if(theta < 1000 and theta > -1000):
            create_drive_direct(speed, speed)
        elif(theta < 1000): # if robot is off to the right then drift to the left
            create_drive_direct(speed - 100, speed + 100)
        else: #if robot is off to the left then drift to the right
            create_drive_direct(speed + 100, speed - 100)
        msleep(10)
        theta += get_theta()

