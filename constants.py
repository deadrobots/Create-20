from wallaby import digital

ROBOT_ID_CLONE = 0
IS_CLONE = digital(ROBOT_ID_CLONE)
IS_PRIME = not IS_CLONE

START_TIME = 0

# servo ports
ARM = 0
HAND = 1

if IS_PRIME:
    # servo positions
    # arm values
    ARM_DOWN = 300
    ARM_POLE_PULL = 600
    ARM_DROP_BOTGUY = 500
    ARM_POLE_GRAB = 700
    ARM_POLE_RELEASE = 700
    ARM_GRAB = 1250
    ARM_SWEEP = 1350
    ARM_UP = 1800

    # hand values
    HAND_OPEN = 80
    HAND_MIDDLE = 800
    HAND_SATELLITE_DROP = 1000
    HAND_CLOSE = 1300

    SWING_GRAB = 400
    SWING_OPEN = 800
    SWING_CLOSE = 1500

    # tophat values
    ON_BLACK = 2000

    # gyro
    TURN_CONVERSION = 5400


elif IS_CLONE:  # placeholder values
    # servo positions
    # arm values
    ARM_DOWN = 10
    ARM_POLE_PULL = 200
    ARM_DROP_BOTGUY = 300
    ARM_POLE_GRAB = 500
    ARM_POLE_RELEASE = 500
    ARM_GRAB = 800
    ARM_UP = 1400

    # hand values
    HAND_OPEN = 80
    HAND_MIDDLE = 800
    HAND_CLOSE = 1300

    SWING_GRAB = 400
    SWING_OPEN = 800
    SWING_CLOSE = 1500

    # top hat values
    ON_BLACK = 2000

    # gyro
    TURN_CONVERSION = 5100
