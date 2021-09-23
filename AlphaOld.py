import RPi.GPIO as GPIO
import time
import random as rnd
import multiprocessing as mp
from pynput.keyboard import Listener, Key


"""def pressed(key):
    print("key pressed: {0}".format(key))
    if key==Key.esc:
        exit()
        
def released(key):
    print("key released: {0}".format(key))
with Listener(on_press=pressed, on_release=released) as listener:
    listener.join()"""


TRIG = 22
ECHO = 27
CTR = 7
BUZ = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(CTR,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(BUZ,GPIO.OUT)

def dist():
	GPIO.output(TRIG,GPIO.HIGH)
	time.sleep(0.000015)
	GPIO.output(TRIG,GPIO.LOW)
	while not GPIO.input(ECHO):
		pass
	t1 = time.time()
	while GPIO.input(ECHO):
		pass
	t2 = time.time()
	return (t2-t1)*34000/2


class AlphaBot2(object):
	
	def __init__(self,ain1=12,ain2=13,ena=6,bin1=20,bin2=21,enb=26):
		self.AIN1 = ain1
		self.AIN2 = ain2
		self.BIN1 = bin1
		self.BIN2 = bin2
		self.ENA = ena
		self.ENB = enb
		self.PA  = 50
		self.PB  = 50

		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.AIN1,GPIO.OUT)
		GPIO.setup(self.AIN2,GPIO.OUT)
		GPIO.setup(self.BIN1,GPIO.OUT)
		GPIO.setup(self.BIN2,GPIO.OUT)
		GPIO.setup(self.ENA,GPIO.OUT)
		GPIO.setup(self.ENB,GPIO.OUT)
		self.PWMA = GPIO.PWM(self.ENA,100)
		self.PWMB = GPIO.PWM(self.ENB,100)
		self.PWMA.start(self.PA)
		self.PWMB.start(self.PB)
		self.stop()

	def forward(self):
		self.PWMA.ChangeDutyCycle(self.PA)
		self.PWMB.ChangeDutyCycle(self.PB)
		GPIO.output(self.AIN1,GPIO.LOW)
		GPIO.output(self.AIN2,GPIO.HIGH)
		GPIO.output(self.BIN1,GPIO.LOW)
		GPIO.output(self.BIN2,GPIO.HIGH)


	def stop(self):
		self.PWMA.ChangeDutyCycle(0)
		self.PWMB.ChangeDutyCycle(0)
		GPIO.output(self.AIN1,GPIO.LOW)
		GPIO.output(self.AIN2,GPIO.LOW)
		GPIO.output(self.BIN1,GPIO.LOW)
		GPIO.output(self.BIN2,GPIO.LOW)

	def backward(self):
		self.PWMA.ChangeDutyCycle(self.PA)
		self.PWMB.ChangeDutyCycle(self.PB)
		GPIO.output(self.AIN1,GPIO.HIGH)
		GPIO.output(self.AIN2,GPIO.LOW)
		GPIO.output(self.BIN1,GPIO.HIGH)
		GPIO.output(self.BIN2,GPIO.LOW)

		
	def left(self):
		self.PWMA.ChangeDutyCycle(30)
		self.PWMB.ChangeDutyCycle(30)
		GPIO.output(self.AIN1,GPIO.HIGH)
		GPIO.output(self.AIN2,GPIO.LOW)
		GPIO.output(self.BIN1,GPIO.LOW)
		GPIO.output(self.BIN2,GPIO.HIGH)


	def right(self):
		self.PWMA.ChangeDutyCycle(30)
		self.PWMB.ChangeDutyCycle(30)
		GPIO.output(self.AIN1,GPIO.LOW)
		GPIO.output(self.AIN2,GPIO.HIGH)
		GPIO.output(self.BIN1,GPIO.HIGH)
		GPIO.output(self.BIN2,GPIO.LOW)
		
	def setPWMA(self,value):
		self.PA = value
		self.PWMA.ChangeDutyCycle(self.PA)

	def setPWMB(self,value):
		self.PB = value
		self.PWMB.ChangeDutyCycle(self.PB)	
		
	def setMotor(self, left, right):
		if((right >= 0) and (right <= 100)):
			GPIO.output(self.AIN1,GPIO.HIGH)
			GPIO.output(self.AIN2,GPIO.LOW)
			self.PWMA.ChangeDutyCycle(right)
		elif((right < 0) and (right >= -100)):
			GPIO.output(self.AIN1,GPIO.LOW)
			GPIO.output(self.AIN2,GPIO.HIGH)
			self.PWMA.ChangeDutyCycle(0 - right)
		if((left >= 0) and (left <= 100)):
			GPIO.output(self.BIN1,GPIO.HIGH)
			GPIO.output(self.BIN2,GPIO.LOW)
			self.PWMB.ChangeDutyCycle(left)
		elif((left < 0) and (left >= -100)):
			GPIO.output(self.BIN1,GPIO.LOW)
			GPIO.output(self.BIN2,GPIO.HIGH)
			self.PWMB.ChangeDutyCycle(0 - left)

#####################################################################################

def main():
    print("Number of CPU: ", mp.cpu_count())

main()


"""if __name__ == '__main__':   
   
    while True:
        try:
            pressed(key)
        except KeyboardInterrupt:
            GPIO.cleanup()
 
    Ab = AlphaBot2()
    Ab.setPWMA(20)
    Ab.setPWMB(20)  
    time.sleep(5)
    
    #set speed of two motors (min 0 , max 100)
    
    while True:
        if GPIO.input(CTR) == 0: 
            btnState=1
        if btnState==1:
            Ab.forward()
            # speed up & sleep down
            speed=10
            for i in range(7):
                Ab.setPWMA(speed)
                Ab.setPWMB(speed)
                time.sleep(1)
                speed = speed+10
            for i in range(7):
                Ab.setPWMA(speed)
                Ab.setPWMB(speed)
                time.sleep(1)
                speed = speed-10 
            Ab.stop()
            
            num = rnd.randrange(2)
            print("num: %d" % num)
            # turn 90 deg left or right
            if dist() < 20:
                #beep_on()
                Ab.stop()
                if num == 0:
                    Ab.left()
                else:
                    Ab.right()
                time.sleep(0.21) #0.21 sec to turn 90 deg in speed of 20
                Ab.stop()
                timecount+=1
                if timecount >= 5: #stop after 5 times
                    break
            try:
                #while True:
                    #print "Distance:%0.2f cm" % dist()     #print distance
                    time.sleep(1)
            except KeyboardInterrupt:
                GPIO.cleanup()
        
    GPIO.cleanup() """
