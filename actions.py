from wallaby import *
import constants as c
import utilities as u
import drive as d
import gyro as g


def init():
    if c.IS_PRIME:
        print("i am prime :)")
    if c.IS_CLONE:
        print("i am clone :)")
    print("trying to connect...")
    create_connect()
    print("connected!")
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
    print("don't touch me, i'm calibrating!")
    g.calibrate_gyro()
    print("calibration complete")
    g.drive_timed(80, 1000)
    msleep(50)
    g.drive_timed(-80, 1000)
    print("aim me!")
    u.wait_for_button()
    u.move_servo(c.ARM, c.ARM_DOWN, 5)
    u.wait_for_button()  # start light
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
    u.move_servo(c.HAND, c.HAND_CLOSE,30)
    u.move_servo(c.ARM, c.ARM_UP,20)
    g.drive_timed(-200, 1000)


def drop_botguy():
    g.turn_with_gyro(-150, 150, 140)
    u.move_servo(c.ARM, c.ARM_DROP_BOTGUY, 5)
    u.move_servo(c.HAND, c.HAND_OPEN)
    u.move_servo(c.ARM, c.ARM_POLE_GRAB)

def go_to_first_pole():
    g.drive_timed(100, 1500)  # drive forward to give room for turn
    g.turn_with_gyro(-50, 50, 84)
    u.move_servo(c.HAND, c.HAND_CLOSE)
    g.drive_timed(100, 500)

def grab_pole():
    g.turn_with_gyro(-50, 50, 80)
    g.drive_timed(100, 2600)
    g.turn_with_gyro(-50, 50, 16)
    # we have the pipe
    u.move_servo(c.ARM, c.ARM_POLE_PULL, 5)
    g.drive_timed(-100, 1500)
    msleep(100)
    g.turn_with_gyro(-50, 50, 14)  # score cart
    msleep(500)
    g.drive_timed(100, 1250) #1300
    u.move_servo(c.ARM, c.ARM_POLE_RELEASE)
    g.turn_with_gyro(50, -50, 40)
    g.drive_timed(-100, 2050) #2000

def go_to_second_pole():
    g.turn_with_gyro(50, -50, 75)
    g.drive_timed(100, 2400)

def go_to_third_pole():
    g.turn_with_gyro(50, -50, 75)
    g.drive_timed(175, 2700)
    msleep(500)
    g.drive_timed(-100, 500)

def grab_third_pole():
    g.turn_with_gyro(-50, 50, 85)
    u.move_servo(c.ARM, c.ARM_POLE_GRAB)
    u.move_servo(c.HAND, c.HAND_MIDDLE)
    g.drive_timed(100, 1700)
    u.move_servo(c.HAND, c.HAND_CLOSE)
    # we have the pipe
    u.move_servo(c.ARM, c.ARM_POLE_PULL)
    msleep(500)
    g.drive_timed(-100, 1300)
    msleep(500)
    g.turn_with_gyro(-100, 100, 20)
    u.move_servo(c.HAND, c.HAND_OPEN)
    u.move_servo(c.ARM, c.ARM_POLE_RELEASE)
    u.wait_for_button()

def go_to_orange_ball():
    g.turn_with_gyro(50, -50, 20)
    u.wait_for_button()
    g.drive_timed(-100, 3000)  # should be a back up until back bumper pressed
    u.wait_for_button()
    u.move_servo(c.ARM, c.ARM_POLE_RELEASE + 200)
    u.wait_for_button()
    g.turn_with_gyro(100, -100, 90)
    u.wait_for_button()
    g.drive_timed(100, 1000)
    u.wait_for_button()
    g.drive_timed(-100, 500)
    u.wait_for_button()
    g.turn_with_gyro(50, -50, 150)
    u.wait_for_button()

def grab_orange_ball():
    u.move_servo(c.ARM, c.ARM_POLE_RELEASE + 100)
    u.move_servo(c.HAND, c.HAND_CLOSE, 3)
    u.wait_for_button()
    u.move_servo(c.ARM, c.ARM_UP, 5)


