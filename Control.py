import time

import RPi.GPIO as GPIO

from config.pinConfig import *


def GrapOpen(t=1):
        GPIOsetup()
        print "Debug: GRAP Open t=",t
        GPIO.output(_GrapOpen, On)
        GPIO.output(_GrapClose, Off)
        time.sleep(t)
        GPIO.output(_GrapOpen, Off)
        GPIO.cleanup()
        return()

def GrapClose(t=1):
        GPIOsetup()
        print "Debug: GRAP Open t=",t
        GPIO.output(_GrapClose, On)
        GPIO.output(_GrapOpen, Off)
        time.sleep(t)
        GPIO.output(_GrapClose, Off)
        GPIO.cleanup()
        return()


def AnkleOpen(t=1):
        GPIOsetup()
        print "Test: Ankle Open t=",t
        GPIO.output(_AnkleOpen, On)
        GPIO.output(_AnkleClose, Off)
        time.sleep(t)
        GPIO.output(_AnkleOpen, Off)
        GPIO.cleanup()
        return()

def AnkleClose(t=1):
        GPIOsetup()
        print "Test: Ankle CLOSE t=",t
        GPIO.output(_AnkleClose, On)
        GPIO.output(_AnkleOpen, Off)
        time.sleep(t)
        GPIO.output(_AnkleClose, Off)
        GPIO.cleanup()
        return()

def BaseCW(t=1):
        GPIOsetup()
        print "Test: Base Move Clock-wise t=", t
        GPIO.output(_BaseCW, On)
        GPIO.output(_BaseCCW, Off)
        time.sleep(t)
        GPIO.output(_BaseCW, Off)
        GPIO.cleanup()
        return()

def BaseCCW(t=1):
        GPIOsetup()
        print "Test: Base Move Counter-Clock-wise t=",t
        GPIO.output(_BaseCCW, On)
        GPIO.output(_BaseCW, Off)
        time.sleep(t)
        GPIO.output(_BaseCCW, Off)
        GPIO.cleanup()
        return()

def AnkelCW(t=1):
        GPIOsetup()
        print "Test: Base Move Clock-wise t=",t
        GPIO.output(_AnkelCW, On)
        GPIO.output(_AnkelCCW, Off)
        time.sleep(t)
        GPIO.output(_AnkelCW, Off)
        GPIO.cleanup()
        return()

def AnkelCCW(t=1):
        GPIOsetup()
        print "Test: Base Move Counter-Clock-wise t=",t
        GPIO.output(_AnkelCCW, On)
        GPIO.output(_AnkelCW, Off)
        time.sleep(t)
        GPIO.output(_AnkelCCW, Off)
        GPIO.cleanup()
        return()
