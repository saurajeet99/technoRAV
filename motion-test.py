import time

from gpiozero import MotionSensor


pir = MotionSensor(4)
sum=0
while True:
    if pir.motion_detected:
        
        print('object is in motion')
        time.sleep(0.5)
