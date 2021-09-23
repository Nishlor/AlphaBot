from pynput.keyboard import Listener,Key
import multiprocessing
import time
    
def pressed(key):
    print("key pressed: {0}".format(key))
    if key==Key.esc:
        exit()
        
def released(key):
    print("key released: {0}".format(key))

def do_something():
    while True:
        print("hi")
        time.sleep(1)

def ourListener():
    with Listener(on_press=pressed, on_release=released) as listener:
        listener.join()
 
p1=multiprocessing.Process(target=do_something)
p2=multiprocessing.Process(target=ourListener)
p2.start()
p1.start()
p1.join()
p2.join()
