import time

from python import _pinConfig

## Unit test before intregrate with html

print "Debug: Initialization "
_pinConfig.Init()

print "Debug: Scenario 1 : Normal"
_pinConfig.doGrapOpen()
time.sleep(5)
_pinConfig.stopGrap()

print "Debug: Scenario 2 : Interupt"
_pinConfig.doGrapClose()
time.sleep(2)
_pinConfig.doGrapOpen()
time.sleep(2)
_pinConfig.stopGrap()

print "Debug: Scenario 3 : No Close 10 sec"
_pinConfig.doGrapClose()
time.sleep(2)
_pinConfig.doGrapOpen()
_pinConfig.doGrapClose()
time.sleep(10)
print "Debug: Ending 3 "
_pinConfig.stopGrap()

