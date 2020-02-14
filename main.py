#!/usr/bin/python
import os, sys
from wallaby import *
import actions as a
import utilities as u
import drive as d
import gyro as g


def main():
    print("Running!!!")
    a.init()
    a.head_to_botguy()
    a.grab_botguy()
    a.drop_botguy()
    a.grab_pole()
    u.DEBUG()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
