# Charging-Monitor

1️⃣ Install Dependencies

Open Command Prompt and install the required package:

pip install psutil plyer

2️⃣ Save the Python Script

Copy the Battery_Monitor.py script 

Save it in a folder 

3️⃣ Create a .BAT File (Runs Silently)
Open Notepad and paste this:

@echo off

pythonw "Path of the file eg. C:\BatteryMonitor\battery_monitor.py"

Save it as battery_monitor.bat in the same folder.

4️⃣ Run Automatically on Startup (Task Scheduler)

Open Task Scheduler (Press Win + R, type taskschd.msc, and hit Enter Or Just search).

Click Create Basic Task → Name it Battery Monitor → Click Next.

Select When I log on → Click Next.

Select Start a Program → Browse for battery_monitor.bat.

Click Finish.


✅ Done! Now it will run automatically at startup and stay in the background. 🚀
