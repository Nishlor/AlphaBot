"""      path for terminal (copy and paste there):
cd AlphaBot2
cd python
cd AlphaProject
python3 AlphaMain.py
"""

import AlphaMotors as am
from pynput.keyboard import Listener,Key
import multiprocessing
import random

speed=20
#to define the alphabot
ab = am.AlphaBot2()
ab.setPWMA(speed)
ab.setPWMB(speed)
#****keyboard functions****************************************
def pressed(key):
    #print("key pressed: {0}".format(key))
#    if key==Key.esc:
#        exit()
    if key==Key.left:
        ab.left()
    if key==Key.right:
        ab.right()
    if key==Key.up:
        ab.forward()
    if key==Key.down:
        ab.stop()
    
def released(key):
    print("key released: {0}".format(key))
    #ab.forward()
#**************************************************************
def turn():
    #num = am.rnd.randrange(2)
    num=0
    ab.stop()
    if num == 0:
        ab.left() 
    else:
        ab.right()
    am.time.sleep(0.23) #0.23 sec to turn 90 deg in speed of 20
    ab.stop()
    ab.forward()  

#****Main******************************************************
def main():
    ab.forward()
    while True:
        try:
            #am.time.sleep(1)
            if am.dist() < 30:
                am.beep_on()
                turn()
                am.beep_off()
            
        except KeyboardInterrupt:
            am.GPIO.cleanup()
            exit()
#*************************************************************
#****multi-processing listener definition and start***********
def ourListener():
    with Listener(on_press=pressed, on_release=released) as listener:
        listener.join()
 
p1=multiprocessing.Process(target=main)
p2=multiprocessing.Process(target=ourListener)
p2.start()
p1.start()
p1.join()
p2.join()
#*************************************************************