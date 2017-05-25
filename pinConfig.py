
import RPi.GPIO as GPIO

# Rasberry pi GPIO pin config

_GrapOpen = 17
_GrapClose = 18
_AnkleOpen = 27
_AnkleClose = 22
_BaseCW = 23
_BaseCCW = 24
_AnkleCW = 10
_AnkleCCW = 9

On = 0
Off = 1

#Setup GPIO
def GPIOsetup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        #set to output mode
        GPIO.setup(_GrapOpen, GPIO.OUT)
        GPIO.setup(_GrapClose, GPIO.OUT)
        GPIO.setup(_AnkleOpen, GPIO.OUT)
        GPIO.setup(_AnkleClose, GPIO.OUT)
        GPIO.setup(_BaseCW, GPIO.OUT)
        GPIO.setup(_BaseCCW, GPIO.OUT)
        GPIO.setup(_AnkleCW, GPIO.OUT)
        GPIO.setup(_AnkleCCW, GPIO.OUT)
        
        
        


def AllOff():
        # Turn off all
        GPIO.output(_GrapOpen, Off)
        GPIO.output(_GrapClose, Off)
        GPIO.output(_AnkleOpen, Off)
        GPIO.output(_AnkleClose, Off)
        GPIO.output(_BaseCW, Off)
        GPIO.output(_BaseCCW, Off)
        GPIO.output(_AnkleCW, Off)
        GPIO.output(_AnkleCCW, Off)

def Init():
    GPIOsetup()
    AllOff()


## MOVING ##


def doGrapOpen():
    GPIOsetup()
    print "Debug: GRAP Open"
    GPIO.output(_GrapOpen, On)
    GPIO.output(_GrapClose, Off)

def doGrapClose():
    GPIOsetup()
    print "Debug: GRAP Close"
    GPIO.output(_GrapClose, On)
    GPIO.output(_GrapOpen, Off)

def doAnkleOpen():
    GPIOsetup()
    print "Debug: Ankle Open"
    GPIO.output(_AnkleOpen, On)
    GPIO.output(_AnkleClose, Off)

def doAnkleClose():
    GPIOsetup()
    print "Debug: Ankle Close"
    GPIO.output(_AnkleClose, On)
    GPIO.output(_AnkleOpen, Off)

def doBaseCW():
    GPIOsetup()
    print "Debug: Base Move Clock-wise"
    GPIO.output(_BaseCW, On)
    GPIO.output(_BaseCCW, Off)

def doBaseCCW():
    GPIOsetup()
    print "Debug: Base Move Counter-Clock-wise"
    GPIO.output(_BaseCCW, On)
    GPIO.output(_BaseCW, Off)

def doAnkelCW():
    GPIOsetup()
    print "Debug: Ankle Move Clock-wise"
    GPIO.output(_AnkleCW, On)
    GPIO.output(_AnkleCCW, Off)

def doAnkelCCW():
    GPIOsetup()
    print "Debug: Ankle Move Counter-Clock-wise"
    GPIO.output(_AnkleCCW, On)
    GPIO.output(_AnkleCW, Off)


## Stop ##

def stopGrap():
    print "Debug: GRAP Stop"
    GPIO.output(_GrapOpen, Off)
    GPIO.output(_GrapClose, Off)
    GPIO.cleanup()

def stopAnkle():
    print "Debug: Ankle Stop"
    GPIO.output(_AnkleClose, Off)
    GPIO.output(_AnkleOpen, Off)
    GPIO.cleanup()

def stopBaseCW():
    print "Debug: Base Stop Turn"
    GPIO.output(_BaseCW, Off)
    GPIO.output(_BaseCCW, Off)
    GPIO.cleanup()

def stopAnkelCW():
    print "Debug: Ankle Stop Turn"
    GPIO.output(_AnkleCCW, Off)
    GPIO.output(_AnkleCW, Off)
    GPIO.cleanup()
