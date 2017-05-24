

import RPi.GPIO as GPIO
import time
from pinConfig import *


def GrapOpen():
        GPIOsetup()
        print "Test: GRAP Open"
        GPIO.output(_GrapOpen, On)
        GPIO.output(_GrapClose, Off)
        time.sleep(5)
        GPIO.output(_GrapOpen, Off)
        GPIO.cleanup()
        return()

def GrapClose():
        GPIOsetup()
        print "Test: GRAP CLOSE"
        GPIO.output(_GrapClose, On)
        GPIO.output(_GrapOpen, Off)
        time.sleep(5)
        GPIO.output(_GrapClose, Off)
        GPIO.cleanup()
        return()

def AnkleOpen():
        GPIOsetup()
        print "Test: Ankle Open"
        GPIO.output(_AnkleOpen, On)
        GPIO.output(_AnkleClose, Off)
        time.sleep(10)
        GPIO.output(_AnkleOpen, Off)
        GPIO.cleanup()
        return()

def AnkleClose():
        GPIOsetup()
        print "Test: Ankle CLOSE"
        GPIO.output(_AnkleClose, On)
        GPIO.output(_AnkleOpen, Off)
        time.sleep(10)
        GPIO.output(_AnkleClose, Off)
        GPIO.cleanup()
        return()

def BaseCW():
        GPIOsetup()
        print "Test: Base Move Clock-wise"
        GPIO.output(_BaseCW, On)
        GPIO.output(_BaseCCW, Off)
        time.sleep(10)
        GPIO.output(_BaseCW, Off)
        GPIO.cleanup()
        return()

def BaseCCW():
        GPIOsetup()
        print "Test: Base Move Counter-Clock-wise"
        GPIO.output(_BaseCCW, On)
        GPIO.output(_BaseCW, Off)
        time.sleep(10)
        GPIO.output(_BaseCCW, Off)
        GPIO.cleanup()
        return()

def AnkelCW():
        GPIOsetup()
        print "Test: Base Move Clock-wise"
        GPIO.output(_AnkelCW, On)
        GPIO.output(_AnkelCCW, Off)
        time.sleep(5)
        GPIO.output(_AnkelCW, Off)
        GPIO.cleanup()
        return()

def AnkelCCW():
        GPIOsetup()
        print "Test: Base Move Counter-Clock-wise"
        GPIO.output(_AnkelCCW, On)
        GPIO.output(_AnkelCW, Off)
        time.sleep(5)
        GPIO.output(_AnkelCCW, Off)
        GPIO.cleanup()
        return()

def TestJoint():
        print "Initilize Joint Arm Test\n==================\n"
        GrapOpen()
        GrapClose()
        AnkleOpen()
        AnkleClose()
        BaseCW()
        BaseCCW()
        AnkelCW()
        AnkelCCW()
        print "\nEND Joint Arm Test\n=================="
        return()

TestJoint()
