# @file: batterylife_checker.py
# @author: Monika

import psutil
from plyer import notification
import time

# create battery sensor object
battery=psutil.sensors_battery()
while True:
    # get current battery state
    percent=battery.percent
    
    # if battery is too low, throw a notification
    if percent <= 20:
        notification.notify(
            title="Battery Percentage",
            message=f"{percent}% battery remaining",
            timeout=10
        )
        break

    # check once in 5 minutes
    time.sleep(60*5)
