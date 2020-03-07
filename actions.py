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
    print("testing bumpers")
    print("left bump")
    while d.get_bump_left() == False:
        pass
    print("right bump")
    while d.get_bump_right() == False:
        pass
    msleep(500)
    print("left or right bump")
    while d.get_bump_left_or_right() == False:
        pass
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


def go_to_first_pole():
    u.move_servo(c.ARM, c.ARM_UP)
    d.drive_to_black_and_square_up(100)
    g.drive_timed(-100, 1500)
    u.move_servo(c.ARM, c.ARM_POLE_GRAB)
    g.turn_with_gyro(-80, 80, 90)
    u.move_servo(c.HAND, c.HAND_CLOSE)
    g.drive_timed(100, 750)
    g.turn_with_gyro(-80, 80, 85)


def first_pole_alt():
    u.move_servo(c.ARM, c.ARM_UP)
    g.turn_with_gyro(-80, 80, 90)
    g.drive_timed(250, 3000)
    g.drive_timed(-250, 2400) #2450
    g.turn_with_gyro(-80, 80, 90)
    d.drive_to_black_and_square_up(-100)
    u.move_servo(c.ARM, c.ARM_POLE_GRAB)
    g.drive_timed(100, 1900)
    msleep(1000)
    u.move_servo(c.HAND, c.HAND_CLOSE)
    u.move_servo(c.ARM, c.ARM_POLE_PULL)
    msleep(500)
    g.drive_timed(-100, 1770) #1750
    g.turn_with_gyro(-50, 50, 15) #15
    msleep(500)
    g.drive_timed(100, 600)
    msleep(500)
    u.move_servo(c.HAND, c.HAND_OPEN)
    u.move_servo(c.ARM, c.ARM_POLE_RELEASE)
    g.turn_with_gyro(50, -50, 15)


def grab_pole():
    g.drive_timed(100, 2200)
    g.turn_with_gyro(-80, 80, 15)
    # we have the pipe
    u.move_servo(c.ARM, c.ARM_POLE_PULL, 5)
    g.drive_timed(-100, 1600)
    msleep(100)
    g.turn_with_gyro(-50, 50, 15)  # score cart
    msleep(500)
    g.drive_timed(100, 1250)
    msleep(500)
    u.move_servo(c.ARM, c.ARM_POLE_RELEASE)
    g.turn_with_gyro(50, -50, 30)
    d.drive_to_black_and_square_up(-100)
    u.move_servo(c.ARM, c.ARM_UP)
    g.drive_timed(200, 500)
    d.drive_to_black_and_square_up(-100)


def go_to_second_pole():
    g.turn_with_gyro(80, -80, 90)
    g.drive_timed(100, 2600)
    g.turn_with_gyro(-80, 80, 85)
    g.drive_timed(100, 500)


def second_pole_alt():
    g.turn_with_gyro(80, -80, 90)
    g.drive_timed(250, 2800) #1100
    g.drive_timed(-250, 1200)
    g.turn_with_gyro(-80, 80, 90)
    g.drive_timed(100, 750)
    d.drive_to_black_and_square_up(-100)
    u.move_servo(c.ARM, c.ARM_POLE_GRAB)
    g.drive_timed(100, 1950)
    msleep(1000)
    u.move_servo(c.HAND, c.HAND_CLOSE)
    u.move_servo(c.ARM, c.ARM_POLE_PULL)
    msleep(500)
    g.drive_timed(-100, 1700)
    g.turn_with_gyro(-50, 50, 15)
    msleep(500)
    g.drive_timed(100, 500)
    msleep(500)
    u.move_servo(c.HAND, c.HAND_OPEN)
    u.move_servo(c.ARM, c.ARM_POLE_RELEASE)
    g.turn_with_gyro(50, -50, 15)
    u.move_servo(c.ARM, c.ARM_UP)
    g.drive_timed(200, 500)
    d.drive_to_black_and_square_up(-100)


def go_to_third_pole():
    g.turn_with_gyro(80, -80, 90)
    g.drive_timed(175, 2800)
    msleep(500)
    g.drive_timed(-100, 600)


def grab_third_pole():
    g.turn_with_gyro(-80, 80, 82)    # 85
    u.move_servo(c.ARM, c.ARM_POLE_GRAB)
    u.move_servo(c.HAND, c.HAND_MIDDLE)
    g.drive_timed(50, 3800)
    msleep(1000)
    u.move_servo(c.HAND, c.HAND_CLOSE)
    msleep(1000)
    # we have the pole
    u.move_servo(c.ARM, c.ARM_POLE_PULL)
    msleep(500)
    g.drive_timed(-100, 1800)   # 1600
    msleep(700)
    g.turn_with_gyro(-50, 50, 15)
    msleep(1000)
    g.drive_timed(100, 500)
    msleep(500)
    u.move_servo(c.HAND, c.HAND_OPEN)
    u.move_servo(c.ARM, c.ARM_POLE_RELEASE + 200)


def go_to_orange_ball():
    g.turn_with_gyro(50, -50, 20)
    d.drive_to_black_and_square_up(-100)
    g.drive_condition(100, d.get_bump_left_or_right, False)
    u.move_servo(c.ARM, c.ARM_POLE_RELEASE + 200)
    g.turn_with_gyro(100, -100, 90)
    g.drive_timed(100, 1200)
    g.drive_timed(-100, 500)
    g.turn_with_gyro(80, -80, 152) #


def grab_orange_ball():
    u.move_servo(c.ARM, c.ARM_POLE_RELEASE +70) #+50
    g.drive_timed(50, 800)
    u.move_servo(c.HAND, c.HAND_CLOSE, 3)
    u.move_servo(c.ARM, c.ARM_UP, 5)


def deliver_organge_ball():
    g.turn_with_gyro(80, -80, 120)
    g.drive_timed(100, 1000)
    d.drive_to_black_and_square_up(100)
    g.turn_with_gyro(-80, 80, 90)
    g.drive_timed(100, 4000)
    g.turn_with_gyro(80, -80, 45)
    g.drive_timed(100, 3300) #3500
    g.turn_with_gyro(80, -80, 12)
    u.move_servo(c.ARM, c.ARM_SWEEP, 5)
    msleep(1000)
    g.turn_with_gyro(-80, 80, 60)
    u.move_servo(c.ARM, c.ARM_UP, 5)
    u.move_servo(c.ARM, c.ARM_SWEEP, 5)
    g.turn_with_gyro(80, -80, 60)
    u.move_servo(c.ARM, c.ARM_UP, 5)
    u.move_servo(c.ARM, c.ARM_SWEEP, 5)
    g.turn_with_gyro(-80, 80, 18)
    u.move_servo(c.ARM, c.ARM_GRAB)
    g.drive_timed(-50, 1200)
    u.move_servo(c.HAND, c.HAND_SATELLITE_DROP - 40, 8)
    msleep(500)
    u.move_servo(c. HAND, c.HAND_SATELLITE_DROP + 75)
