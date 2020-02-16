from wallaby import *
import constants as c


def wait_for_button():
    print "Press Button..."
    while not right_button():
        pass
    msleep(1)
    print "Pressed"
    msleep(1000)


def move_servo(servo, end_pos, speed=10):
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = get_servo_position(servo)
    if now > 2047:
        print("Servo setting too large ", servo)
    if now < 0:
        print("Servo setting too small ", servo)
    if now > end_pos:
        speed = -speed
    for i in range(now, end_pos, speed):
        set_servo_position(servo, i)
        msleep(10)
    set_servo_position(servo, end_pos)
    msleep(10)


def DEBUG(print_time=True):
    ao()
    msleep(100)
    if print_time:
        print 'Program stop for DEBUG\nSeconds: ', seconds() - c.START_TIME
    #move_servo(c.ARM, c.ARM_DOWN)
    msleep(2500)
    disable_servos()
    exit(0)
