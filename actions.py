from wallaby import *
import constants as c
import utilities as u

def init():
    create_connect()
    create_full()
    enable_servo(c.ARM)
    enable_servo(c.HAND)

def head_to_botguy():
    u.move_servo(c.ARM, c.ARM_UP)
    u.move_servo(c.HAND, c.HAND_OPEN)
    drive_timed(500, 500, 2000)

def drive_timed(left, right, time): #DRS forward is opposite of create forward
    create_drive_direct(-right, -left)
    msleep(time)
    create_drive_direct(0, 0)

def grab_botguy():
    u.move_servo(c.ARM, c.ARM_GRAB)
    msleep(1000)
    drive_timed(100, 100, 1400)
    u.wait_for_button()
    u.move_servo(c.HAND, c.HAND_CLOSE)
    msleep(1000)
    u.move_servo(c.ARM, c.ARM_UP)
    msleep(1000)
    drive_timed(-200, -200, 1000)
    u.move_servo(c.HAND, c.HAND_OPEN)
