#!/usr/bin/python
from wallaby import *
import wallaby as w
import constants as c
import utilities as u
import drive as d


bias = 0
addition_factor = 1.920137e-16
multiplication_factor = 0.000004470956


def calibrate_gyro():
    i = 0
    avg = 0
    while i < 100:
        avg += w.gyro_z()
        msleep(1)
        i += 1
    global bias
    bias = avg/i
    msleep(60)


def _freeze_motors():
    create_drive_direct(0, 0)


#######################################
# drive functions
# the drive functions use the change in gyro_z to adjust wheel speeds and drive straight

def _drive(speed):
    # calibrate_gyro()
    theta = 0
    while True:
        if speed > 0:
            create_drive_direct(int((speed + speed * (addition_factor + multiplication_factor*theta))),
                                int((speed - speed * (addition_factor + multiplication_factor*theta))))
        else:
            create_drive_direct(int((speed - speed * (addition_factor + multiplication_factor*theta))),
                                int((speed + speed * (addition_factor + multiplication_factor*theta))))
        msleep(10)
        theta += (w.gyro_z() - bias) * 10
    _freeze_motors()


def _drive_left_right(left_speed, right_speed, theta=0):
    # calibrate_gyro()
    if right_speed > 0:
        create_drive_direct(int((left_speed + left_speed * (addition_factor + multiplication_factor * theta))),
                            int((right_speed - right_speed * (addition_factor + multiplication_factor * theta))))
    else:
        create_drive_direct(int((left_speed - left_speed * (addition_factor + multiplication_factor * theta))),
                            int((right_speed + right_speed * (addition_factor + multiplication_factor * theta))))
    msleep(10)


def drive_timed(speed, time):
    # print("driving for time")
    # calibrate_gyro()
    start_time = seconds()
    theta = 0
    speed = -speed
    while seconds() - start_time < time/1000.0:
        if speed > 0:
            create_drive_direct(int((speed + speed * (addition_factor + multiplication_factor*theta))),
                                int((speed - speed * (addition_factor + multiplication_factor*theta))))
        else:
            create_drive_direct(int((speed - speed * (addition_factor + multiplication_factor*theta))),
                                int((speed + speed * (addition_factor + multiplication_factor*theta))))
        msleep(10)
        theta += (w.gyro_z() - bias) * 10
    _freeze_motors()


def drive_timed_left_right(left_speed, right_speed, time):
    # calibrate_gyro()
    # print("driving for time")
    start_time = seconds()
    theta = 0
    while seconds() - start_time < time/1000.0:
        if right_speed > 0:
            create_drive_direct(int((left_speed + left_speed * (addition_factor + multiplication_factor * theta))),
                                int((right_speed - right_speed * (addition_factor + multiplication_factor * theta))))
        else:
            create_drive_direct(int((left_speed - left_speed * (addition_factor + multiplication_factor * theta))),
                                int((right_speed + right_speed * (addition_factor + multiplication_factor * theta))))
        msleep(10)
        theta += (w.gyro_z() - bias) * 10
    _freeze_motors()


def drive_condition(speed, test_function, state=True):  # needs some work
    # this function was written by Charlie, the 2019 season captain
    # calibrate_gyro()
    # print("Driving while condition is inputted state")
    theta = 0
    while test_function() is state:
        if speed > 0:
            create_drive_direct(int((speed + speed * (addition_factor + multiplication_factor*theta))),
                                int((speed - speed * (addition_factor + multiplication_factor*theta))))
        else:
            create_drive_direct(int((speed - speed * (addition_factor + multiplication_factor*theta))),
                                int((speed + speed * (addition_factor + multiplication_factor*theta))))
        msleep(10)
        theta += (w.gyro_z() - bias) * 10
    _freeze_motors()


#######################################
# pivot functions
# all of these turn/pivots measure the change gyro_z to make the turn or pivot more exact

def turn_with_gyro(left_wheel_speed, right_wheel_speed, target_theta_deg):
    # calibrate_gyro()
    # print("turning")
    target_theta = round(target_theta_deg * c.TURN_CONVERSION)
    theta = 0
    while theta < target_theta:
        create_drive_direct(-right_wheel_speed, -left_wheel_speed)
        msleep(10)
        theta += abs(w.gyro_z() - bias) * 10
    # print(theta)
    _freeze_motors()


def pivot_on_left_wheel(left_wheel_speed, target_theta_deg):
    # calibrate_gyro()
    # print("pivoting on left")
    target_theta = round(target_theta_deg * c.TURN_CONVERSION)
    theta = 0
    while theta < target_theta:
        create_drive_direct(-left_wheel_speed, 0)
        msleep(10)
        theta += abs(w.gyro_z() - bias) * 10
    _freeze_motors()


def pivot_on_right_wheel(right_wheel_speed, target_theta_deg):
    # calibrate_gyro()
    # print("pivoting on right")
    target_theta = round(target_theta_deg * c.TURN_CONVERSION)
    theta = 0
    while theta < target_theta:
        create_drive_direct(0, -right_wheel_speed)
        msleep(10)
        theta += abs(w.gyro_z() - bias) * 10
    _freeze_motors()

