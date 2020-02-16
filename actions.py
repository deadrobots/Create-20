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
    msleep(100)
    print("testing arm")
    u.move_servo(c.ARM, c.ARM_UP)
    u.move_servo(c.ARM, c.ARM_DOWN)
    u.move_servo(c.ARM, c.ARM_UP)
    print("testing hand")
    u.move_servo(c.HAND, c.HAND_OPEN)
    u.move_servo(c.HAND, c.HAND_CLOSE)
    u.move_servo(c.HAND, c.HAND_OPEN)
    u.move_servo(c.ARM, c.ARM_DOWN)
    print("don't touch me, i'm calibrating!!")
    g.calibrate_gyro()
    g.drive_timed(80, 1000)
    msleep(100)
    g.drive_timed(-80, 1000)
    u.wait_for_button()
    g.calibrate_gyro()


def head_to_botguy():
    u.move_servo(c.ARM, c.ARM_UP)
    u.move_servo(c.HAND, c.HAND_OPEN)
    g.drive_timed(400, 2400)
    g.pivot_on_left_wheel(100, 42)
    g.drive_timed(100, 1000)
    g.drive_timed(-100, 950)
    g.pivot_on_right_wheel(100, 50)
    u.move_servo(c.ARM, c.ARM_GRAB)
    #u.wait_for_button()
    msleep(100)


def grab_botguy():
    #u.move_servo(c.ARM, c.ARM_GRAB)
    #msleep(100)
    # g.pivot_on_left_wheel(200, 15)
    #u.wait_for_button()
    #u.move_servo(c.ARM, c.ARM_GRAB - 200)
    u.move_servo(c.HAND, c.HAND_CLOSE)
    msleep(100)
    u.move_servo(c.ARM, c.ARM_UP)
    msleep(100)
    g.drive_timed(-200, 1000)


def drop_botguy():
    # d.drive_until_left_bump(100)
    #u.wait_for_button()
    g.turn_with_gyro(-100, 100, 150)
    u.move_servo(c.ARM, c.ARM_DROP_BOTGUY)
    msleep(100)
    u.move_servo(c.HAND, c.HAND_OPEN)
    msleep(100)

def grab_pole():
    g.turn_with_gyro(-100, 100, 80)
    g.drive_timed(100, 1200)
    g.turn_with_gyro(-100, 100, 87)
    # 150 used to be 170 degrees
    u.move_servo(c.ARM, c.ARM_DROP_BOTGUY + 200)
    g.drive_timed(100, 1000)
    u.move_servo(c.HAND, c.HAND_CLOSE)
    # we have the pipe
    #msleep(100)
    # d.drive_to_black_and_square_up(100)
    # msleep(100)
    # u.move_servo(c.ARM, c.SWING_GRAB)
    # msleep(100)
    # u.move_servo(c.HAND, c.SWING_OPEN)
    # msleep(100)
    # print (" time to pivot ")
    # g.drive_timed(100, 2500)
    # g.pivot_on_left_wheel(100, 60)
    # move wrist
    #msleep(100)
    print (" here ")
    u.move_servo(c.ARM, c.ARM_DROP_BOTGUY -100)
    msleep(500)
    g.drive_timed(-100, 1250)
    msleep(500)
    g.turn_with_gyro(-100, 100, 20)
    u.move_servo(c.HAND, c.HAND_OPEN)
    u.move_servo(c.ARM, c.ARM_POLE_RELEASE)
    g.drive_timed(-100, 1200)
    g.turn_with_gyro(100, -100, 110)
    g.drive_timed(100, 1250)







