
import RPi.GPIO as GPIO
import time

_GrapOpen = 17
_GrapClose = 18
_AnkleOpen = 27
_AnkleClose = 22

On = 0
Off = 1

#Setup GPIO
def GPIOsetup():
    GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(_GrapOpen, GPIO.OUT)
        GPIO.setup(_GrapClose, GPIO.OUT)
        GPIO.setup(_AnkleOpen, GPIO.OUT)
        GPIO.setup(_AnkleClose, GPIO.OUT)
        
        GPIO.output(_GrapOpen, Off)
        GPIO.output(_GrapClose, Off)
        GPIO.output(_AnkleOpen, Off)
        GPIO.output(_AnkleClose, Off)

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




GrapOpen()
GrapClose()
AnkleOpen()
AnkleClose()
