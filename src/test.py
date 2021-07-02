#%%
from time import sleep
from drive.mecanum_driver import Direction
from hal.led_driver import LedDriver, Piktogram
from config.device_config import *
ledDriver.ledSet(Piktogram.ruler)
# %%
ledDriver.ledSet(Piktogram.taco)
# %%
from config.device_config import distanceDriver, driver
from drive.mecanum_driver import Direction
from time import sleep
driver.rotate(Direction.right)
sleep(0.7)
driver.stop()
driver.drive(Direction.forward)
sleep(4)
driver.stop()
# %%
from config.device_config import movetofront
movetofront.start()
# %%
