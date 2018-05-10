#!/usr/bin/env python

import pigpio
import sys

red = sys.argv[1]
green = sys.argv[2]
blue = sys.argv[3]

pi = pigpio.pi()

#old 17,24,22
#imma be using 13, 19, 26
#replace first argument below with the GPIO Pin number associated with the specified color
pi.set_PWM_dutycycle(13,red)
pi.set_PWM_dutycycle(19,green)
pi.set_PWM_dutycycle(26,blue)
