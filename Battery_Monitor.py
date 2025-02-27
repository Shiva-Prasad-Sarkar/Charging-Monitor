import psutil
import time
from plyer import notification
import platform

def beep():
    system_name = platform.system()
    if system_name == "Windows":
        import winsound
        winsound.Beep(1000, 500)  
    elif system_name == "Linux":
        import os
        os.system('aplay /usr/share/sounds/freedesktop/stereo/dialog-information.oga')  
    elif system_name == "Darwin":  
        os.system('afplay /System/Library/Sounds/Glass.aiff')

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=5
    )

def monitor_battery():
    prev_status = None
    while True:
        battery = psutil.sensors_battery()
        if battery:
            plugged = battery.power_plugged
            if prev_status is not None and prev_status != plugged:
                if plugged:
                    notify("Charging", "Your device is now plugged in.")
                else:
                    notify("Unplugged", "Your charger has been disconnected!")
                beep()
            prev_status = plugged
        time.sleep(5)  

if __name__ == "__main__":
    monitor_battery()
