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
    # arm
    ARM_DOWN = 100
    ARM_DROP_BOTGUY = 500
    ARM_GRAB = 1250
    ARM_UP = 1800
    # hand
    HAND_OPEN = 80
    HAND_CLOSE = 1300
    SWING_GRAB = 400
    SWING_OPEN = 800
    SWING_CLOSE = 1500

    # top hat values
    ON_BLACK = 2000

    # gyro
    TURN_CONVERSION = 5400


elif IS_CLONE:  # placeholder values
    # servo positions
    ARM_DOWN = 10
    ARM_UP = 1400
    ARM_GRAB = 800
    HAND_OPEN = 80
    HAND_CLOSE = 1300
    ARM_DROP_BOTGUY = 300
    SWING_GRAB = 400
    SWING_OPEN = 800
    SWING_CLOSE = 1500

    # top hat values
    ON_BLACK = 2000

    # gyro
    TURN_CONVERSION = 5100
