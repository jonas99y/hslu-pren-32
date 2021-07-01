#%%
from drive.mecanum_driver import Direction
from hal.led_driver import LedDriver, Piktogram
from config.device_config import *
ledDriver.ledSet(Piktogram.ruler)
# %%
ledDriver.ledSet(Piktogram.taco)
# %%
from config.device_config import distanceDriver
from drive.mecanum_driver import Direction

distanceDriver.drive(Direction.left, 80)
# %%