import time
import pinConfig

## Unit test before intregrate with html

print "Debug: Initialization "
pinConfig.Init()

print "Debug: Scenario 1 : Normal"
pinConfig.doGrapOpen()
time.sleep(5)
pinConfig.stopGrap()

print "Debug: Scenario 2 : Interupt"
pinConfig.doGrapClose()
time.sleep(2)
pinConfig.doGrapOpen()
time.sleep(2)
pinConfig.stopGrap()

print "Debug: Scenario 3 : No Close 10 sec"
pinConfig.doGrapClose()
time.sleep(2)
pinConfig.doGrapOpen()
pinConfig.doGrapClose()
time.sleep(10)
print "Debug: Ending 3 "
pinConfig.stopGrap()

