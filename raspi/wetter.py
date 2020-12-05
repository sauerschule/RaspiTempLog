#!/usr/bin/python3

# You have to run this before running this script:
# sudo pip3 install adafruit-circuitpython-am2320
# See also: https://learn.adafruit.com/adafruit-am2320-temperature-humidity-i2c-sensor/python-circuitpython

import time
import board
import busio
import adafruit_am2320
import datetime

# create the I2C shared bus
i2c = busio.I2C(board.SCL, board.SDA)
am = adafruit_am2320.AM2320(i2c)

temp = am.temperature
hum = am.relative_humidity
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

time.sleep(0.1)
print("%s;%2.1f;%2.1f" % (date,temp,hum) )
