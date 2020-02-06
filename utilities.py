from wallaby import *
import constants as c

def wait_for_button():
    print "Press Button..."
    while not right_button():
        pass
    msleep(1)
    print "Pressed"
    msleep(1000)


def move_servo(servo, endPos, speed=10):
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = get_servo_position(servo)
    if now > 2047:
        print("Servo setting too large ", servo)
    if now < 0:
        print("Servo setting too small ", servo)
    if now > endPos:
        speed = -speed
    for i in range(now, endPos, speed):
        set_servo_position(servo, i)
        msleep(10)
    set_servo_position(servo, endPos)
    msleep(10)

def DEBUG(PrintTime=True):
    wait_for_button()
    ao()
    msleep(100)
    if PrintTime:
        print 'Program stop for DEBUG\nSeconds: ', seconds() - c.START_TIME
    move_servo(c.ARM, c.ARM_DOWN)
    msleep(2500)
    disable_servos()
    exit(0)