#!/usr/bin/python3
# Run the O2 sensor  reading 30 time per minute

import os, time

cmd = '/usr/bin/python3 /home/pi/Work/RS485/O2/run.py'
for t in range(1, 60, 30):
    #print(t)
    os.system(cmd)
    time.sleep(2)
