from wallaby import *
import constants as c
import utilities as u
import drive as d
import gyro as g


def init():
    create_connect()
    create_full()
    enable_servo(c.ARM)
    enable_servo(c.HAND)


def head_to_botguy():
    u.move_servo(c.ARM, c.ARM_UP)
    u.move_servo(c.HAND, c.HAND_OPEN)
    d.drive_timed(500, 500, 2200)
    msleep(1000)


def grab_botguy():
    u.move_servo(c.ARM, c.ARM_GRAB)
    msleep(1000)
    msleep(1000)
    d.drive_timed(50, 100, 400)
    u.move_servo(c.ARM, c.ARM_GRAB-200)
    msleep(1000)
    u.move_servo(c.HAND, c.POLE_CLOSE)
    msleep(1000)
    u.move_servo(c.ARM, c.ARM_UP)
    msleep(1000)
    d.drive_timed(-200, -200, 1000)


def drop_botguy():
    #d.drive_until_left_bump(100)
    d.drive_timed(-200, -200, 4000)
    msleep(1000)
    d.drive_timed(50, -50, 1500)
    msleep(1000)
    d.drive_to_black_and_square_up(100)
    msleep(1000)
    d.rotate(100, 3000)
    msleep(1000)
    u.move_servo(c.ARM, c.DROP_BOTGUY)
    msleep(1000)
    u.move_servo(c.HAND, c.HAND_OPEN)
    msleep(1000)
    d.rotate(100, 3000)
    msleep(1000)
    d.drive_to_black_and_square_up(100)
    msleep(1000)

def grab_pole():
    u.move_servo(c.ARM, c.POLE_GRAB)
    msleep(500)
    u.move_servo(c.HAND, c.POLE_OPEN)
    msleep(500)
    d.drive_timed(100, 100, 2500)
    # move wrist
    msleep(1000)
    u.move_servo(c.HAND, c.HAND_CLOSE)
    msleep(500)
    d.drive_timed(-100, -100, 1000)


