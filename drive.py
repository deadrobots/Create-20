from wallaby import *
from math import pi
import constants as c
import utilities as u


def get_bump_left():
    """Returns condition of left create bumper"""
    return get_create_lbump


def get_bump_right():
    """Returns condition of right create bumper"""
    return get_create_rbump


def drive_until_left_bump(speed):
    while not get_bump_left():
        create_drive_direct(speed, speed)
    create_drive_direct(0, 0)
    print("left bumped")


def drive_until_right_bump(speed):
    while not get_bump_right():
        create_drive_direct(speed, speed)
    create_drive_direct(0, 0)
    print("right bumped")


def get_black_right():
    #print("Black Right Cliff")
    return get_create_rcliff_amt() < c.ON_BLACK


def get_black_left():
    #print("Black Left Cliff")
    #print("Black Left Cliff")
    return get_create_lcliff_amt() < c.ON_BLACK


def get_left_front():
    return get_create_lfcliff_amt() < c.ON_BLACK


def get_right_front():
    return get_create_rfcliff_amt() < c.ON_BLACK


def black_left_or_right():
    return get_black_left() or get_black_right()


def black_left_and_right():
    return get_black_left() and get_black_right()


def black_left_and_right_front():
    return get_left_front() and get_right_front()


def drive_to_black_and_square_up(speed):
    speed = -speed
    while not black_left_and_right():
        if get_black_left():
            create_drive_direct(0, speed)
        elif get_black_right():
            create_drive_direct(speed, 0)
        else:
            create_drive_direct(speed, speed)
    create_drive_direct(0, 0)


def drive_timed(left, right, time): #DRS forward is opposite of create forward
    create_drive_direct(-right, -left)
    msleep(time)
    create_drive_direct(0, 0)


def drive_condition(condition, speed):
    #print("Driving for condition")
    speed = -speed
    create_drive_direct(speed, speed)
    while condition:
         pass
    create_drive_direct(0, 0)


def spin_cw(power, time):
    create_drive_direct(power, -power)
    msleep(time)
    create_drive_direct(0, 0)


def spin_ccw(power, time):
    create_drive_direct(-power, power)
    msleep(time)
    create_drive_direct(0, 0)


def rotate(power, time):
    if power > 0:
        spin_ccw(power, time)
    else:
        spin_cw(abs(power), time)


def rotate_till_black(power):
    if power > 0:
        create_drive_direct(-power, power)
    else:
        create_drive_direct(power, -power)
    while (get_create_rfcliff_amt() > 2000):
        pass
    create_stop()


def drive_forever(left, right):
    create_drive_direct(-right, -left)


def stop():
    create_stop()


INCH_TO_MIL = 25.4


def drive_distance2(distance, speed):
    if distance < 0:
        speed = -speed
    dist_mil = INCH_TO_MIL * distance
    time = (int)((dist_mil / speed) * 1000)
    drive_timed(speed, speed, time)


def rotate_degrees(degrees, speed):
    if degrees < 0:
        speed = -speed
        degrees = abs(degrees)
    degrees = degrees * 1.13
    set_create_total_angle(0)
    drive_forever(-speed, speed)
    while abs(get_create_total_angle()) < degrees:
        pass
    stop()


def pivot_till_black(power):
    if power > 0:
        create_drive_direct(0, -power)
    else:
        create_drive_direct(0, power)
    while analog(c.left_tophat) < 2000:
        pass
    create_stop()


def timed_line_follow_left_front(speed, time):
    sec = seconds()
    while(seconds() - sec<time):
        if get_left_front():
            create_drive_direct(speed/10, speed)
        else:
            create_drive_direct(speed, speed/10)
        msleep(10)
    create_stop()


def turn_till_right_front_black(left, right):
    create_drive_direct(left, right)
    while (get_create_rfcliff_amt() > 2000):
        pass
    create_stop()


def proportional_line_follow(speed, time):
    sec = seconds()
    while(seconds() - sec<time):
        if get_create_lfcliff_amt() < 1200:
            create_drive_direct(speed, speed/15)
        elif get_create_lfcliff_amt < 1700 and get_create_lfcliff_amt > 1200:
            create_drive_direct(speed, speed/10)
        elif get_create_lfcliff_amt < 2200 and get_create_lfcliff_amt > 1700:
            create_drive_direct(speed, speed)
        elif get_create_lfcliff_amt < 2700 and get_create_lfcliff_amt > 2200:
            create_drive_direct(speed/2, speed)
        elif get_create_lfcliff_amt > 2700:
            create_drive_direct(speed/5, speed)
        msleep(10)
    create_drive_direct(0, 0)
