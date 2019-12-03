#run this file from terminal
#must be in the same folder on the Pi as servomotor4.py
import motor
from socket import *
import time
from time import ctime
import RPi.GPIO as GPIO
import Adafruit_PCA9685

#Initializing the I2C communication with servo hat
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#Run initial setup
motor.setup(pwm)

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)
tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    try:
        
        #print 'waiting for connection'
        tcpSerSock.settimeout(2)
        tcpCliSock,addr = tcpSerSock.accept()
        '...connected from :', addr
        
        try:
            while True:
                cardata = ''
                cardata = tcpCliSock.recv(BUFSIZE)
                if not cardata:
                    break

                #split the string
                cardata.split("||")
                s,t,u,l,r = cardata.split("||")
                #change back to numeric value
                steerpi = float(s)
                speedpi = float(t)
                UpDownLevel = float(u)
                LeftRightLevel = float(l)
                StartStop = int(float(r))
                #heart = int(float(h))

                motor.test(speedpi,StartStop,pwm)
                motor.steertest(steerpi, pwm)
                motor.cameraboi(UpDownLevel, LeftRightLevel, pwm)

                #Use the above line for the other variables
                #and write a method in motor.py to match
                print('Steering Angle: ',steerpi)
                print('Throttle %: ',speedpi)
                print('U/D Cam Servo Pulse Width: ', UpDownLevel)
                print('L/R Cam Servo Pulse Width: ', LeftRightLevel)
                print('Run Status(1 = Run): ', StartStop)
                #print 'Heartbeat: ',heart
        
        except KeyboardInterrupt:
            motor.close()
            GPIO.cleanup()
            pass

    except timeout:
        motor.timeout(pwm)
        time.sleep(1)
        
tcpSerSock.close()
