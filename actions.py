from wallaby import *
import constants as c
import utilities as u
import drive as d
import gyro as g


def init():
    if c.IS_PRIME:
        print("i am prime:)")
    if c.IS_CLONE:
        print("i am clone:)")
    create_connect()
    print("Connected!!")
    create_full()
    enable_servos()
    print("testing arm")
    u.move_servo(c.ARM, c.ARM_UP, 5)
    u.move_servo(c.ARM, c.ARM_DOWN, 5)
    u.move_servo(c.ARM, c.ARM_UP, 5)
    print("testing hand")
    u.move_servo(c.HAND, c.HAND_OPEN, 5)
    u.move_servo(c.HAND, c.HAND_CLOSE, 5)
    u.move_servo(c.HAND, c.HAND_OPEN, 5)
    u.move_servo(c.ARM, c.ARM_DOWN, 5)
    print("don't touch me, i'm calibrating!!")
    g.calibrate_gyro()
    g.drive_timed(80, 1000)
    msleep(50)
    g.drive_timed(-80, 1000)
    u.wait_for_button()
    c.START_TIME = seconds()
    g.calibrate_gyro()


def head_to_botguy_slow():
    u.move_servo(c.ARM, c.ARM_UP)
    u.move_servo(c.HAND, c.HAND_OPEN)
    g.drive_timed(400, 2400)
    g.pivot_on_left_wheel(100, 42)
    g.drive_timed(100, 1000)
    g.drive_timed(-100, 950)
    g.pivot_on_right_wheel(100, 50)
    u.move_servo(c.ARM, c.ARM_GRAB)
    msleep(100)

def head_to_botguy_fast():
    print "head_to_botguy_fast"
    u.move_servo(c.ARM, c.ARM_UP,50)
    u.move_servo(c.HAND, c.HAND_OPEN,50)
    g.drive_timed(500, 2300)
    u.move_servo(c.ARM, c.ARM_GRAB)


def grab_botguy():
    #u.move_servo(c.ARM, c.ARM_GRAB)
    #msleep(100)
    # g.pivot_on_left_wheel(200, 15)
    #u.wait_for_button()
    #u.move_servo(c.ARM, c.ARM_GRAB - 200)
    u.move_servo(c.HAND, c.HAND_CLOSE,30)
    u.move_servo(c.ARM, c.ARM_UP,20)
    g.drive_timed(-200, 1000)


def drop_botguy():
    # d.drive_until_left_bump(100)
    #u.wait_for_button()
    g.turn_with_gyro(-150, 150, 140)
    u.move_servo(c.ARM, c.ARM_DROP_BOTGUY)
    u.move_servo(c.HAND, c.HAND_OPEN)
    u.move_servo(c.ARM, c.ARM_POLE_GRAB)

def go_to_first_pole():
    g.drive_timed(100, 1500)
    g.turn_with_gyro(-100, 100, 83)
    u.move_servo(c.HAND, c.HAND_CLOSE)
    g.drive_timed(100, 1200)

def grab_first_pole():
    g.turn_with_gyro(-100, 100, 87)
    g.drive_timed(100, 2500)
    g.turn_with_gyro(-100, 100, 20)
    # we have the pipe
    u.move_servo(c.ARM, c.ARM_DROP_BOTGUY - 100)
    g.drive_timed(-100, 1500)
    msleep(50)
    g.turn_with_gyro(-100, 100, 16) #score cart
    #u.move_servo(c.ARM, c.ARM_POLE_RELEASE)
    g.drive_timed(100, 1300)
    u.move_servo(c.ARM, c.ARM_POLE_RELEASE)
    g.turn_with_gyro(100, -100, 40)
    g.drive_timed(-100, 2000)

def go_to_second_pole():
    g.drive_timed(-100, 1250)
    g.turn_with_gyro(100, -100, 110)
    g.drive_timed(100, 1800)

def grab_second_pole():
    g.turn_with_gyro(-100, 100, 87)
    u.move_servo(c.ARM, c.ARM_POLE_GRAB)
    g.drive_timed(100, 2700)
    u.move_servo(c.HAND, c.HAND_CLOSE)
    # we have the pipe
    u.move_servo(c.ARM, c.ARM_DROP_BOTGUY - 100)
    msleep(500)
    g.drive_timed(-100, 1300)
    msleep(500)
    g.turn_with_gyro(-100, 100, 20)
    u.move_servo(c.HAND, c.HAND_OPEN)
    u.move_servo(c.ARM, c.ARM_POLE_RELEASE)

def go_to_third_pole():
    g.turn_with_gyro(100, -100, 110)
    g.drive_timed(100, 3000)
    g.drive_timed(-100, 500)

def grab_third_pole():
    u.wait_for_button()
    g.turn_with_gyro(-100, 100, 84)
    u.wait_for_button()
    u.move_servo(c.ARM, c.ARM_POLE_GRAB)
    u.move_servo(c.HAND, c.HAND_MIDDLE)
    u.wait_for_button()
    g.drive_timed(100, 1500)
    u.move_servo(c.HAND, c.HAND_CLOSE)
    # we have the pipe
    print (" here ")
    u.move_servo(c.ARM, c.ARM_DROP_BOTGUY - 100)
    msleep(500)
    g.drive_timed(-100, 1300)
    msleep(500)
    g.turn_with_gyro(-100, 100, 20)
    u.move_servo(c.HAND, c.HAND_OPEN)
    u.move_servo(c.ARM, c.ARM_POLE_RELEASE)

def go_to_orange_ball():
    g.drive_timed(-100, 20)
    g.turn_with_gyro(100, -100, 110)
    g.drive_timed(100, 1500)
    g.drive_timed(-100, 2000)
    g.turn_with_gyro(-100, 100, 50)











