#!/usr/bin/env python3
import random
import os
import time
import subprocess

bx=100
by=100
while True:
    rand_1 = random.randint(0, 100)
    if rand_1%2:
      bx += 1
    else:
      bx -= 1
    rand_2 = random.randint(0, 100)
    if rand_2%2:
      by += 1
    else:
      by -= 1

    print(f"'x':{bx},'y':{by}")
    subprocess.run(['mosquitto_pub', '-h', 'mqtt', '-t', 'point', '-m',f"'x':{bx},'y':{by}"])
    time.sleep(1)
