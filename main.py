#!/usr/bin/python
import os, sys
from wallaby import *
import actions as a
import utilities as u

def main():
    print("Running!!!")
    a.init()
    a.head_to_botguy()
    a.grab_botguy()
    u.DEBUG()

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)

    main()