#!/usr/bin/python

from time import sleep
import datetime,random
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate(busnum = 0)

# Cycle through backlight colors
col = (lcd.RED , lcd.YELLOW, lcd.GREEN, lcd.TEAL,
       lcd.BLUE, lcd.VIOLET)

now = None
while True:    
    lcd.clear()      
    now = datetime.datetime.now()
    month = now.month if now.month >= 10 else "0%s" %  str(now.month)
    day = now.day if now.day >= 10 else "0%s" %  str(now.day)
    hour = now.hour if now.hour >= 10 else "0%s" % str(now.hour)
    mins = now.minute if now.minute >= 10 else "0%s" % str(now.minute)
    seconds = now.second if now.second >= 10 else "0%s" % str(now.second)
    lcd.message("%s/%s/%s\n%s:%s:%s" % (month,day,now.year,hour,mins,seconds))    
    sleep(.01)
    lcd.backlight(col[random.randint(0,len(col)-1)])
    sleep(.5)
