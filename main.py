#run this file from terminal
#must be in the same folder on the Pi as servomotor4.py
import motor
import time
from time import ctime
import RPi.GPIO as GPIO
import Adafruit_PCA9685
import keyboard
from picamera import PiCamera
import csv
import os, shutil

# set camera up
camera = PiCamera()
camera.resolution = (208, 160)
camera.framerate = 40
camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 0
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
camera.rotation = 0
camera.hflip = False
camera.vflip = False

#Initializing the I2C communication with servo hat
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#Run initial setup
motor.setup(pwm)

go = False
speedStop = 15
speedGo = 18
debounce = 0
speed = 0
a = 1

# list to hold all data
data = []

index = 0

# start when space is pressed
keyboard.wait("space")

# delete all photos
folder = '/home/pi/neuroDrive/images'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)
        
#startTime = int(round(time.time() * 1000))


# begin main loop
while (True):
    temp = []
    temp.append(index)
    print(index)
    
    if (go == True):
        mod = index%a
        if(mod == 0):
            speed = speedStop
        else:
            speed = speedGo
            
    
#    curTime = int(round(time.time() * 1000))
#    dif = curTime - startTime
    
#    if (go == True):
#        time_pwm = int(dif/50)
#        mod = time_pwm%2
#        if (mod == 0):
#            speed = speedGo
#        else:
#            speed = speedStop
    
    if keyboard.is_pressed('w'): 
        speed = speedGo
        go = True
    elif keyboard.is_pressed('a'):
        speed = speedStop
        go = False
        
    if keyboard.is_pressed('1'): 
        a = 1
    elif keyboard.is_pressed('2'):
        a = 2
    elif keyboard.is_pressed('3'):
        a = 3
    elif keyboard.is_pressed('4'):
        a = 4
    elif keyboard.is_pressed('5'):
        a = 5

    if keyboard.is_pressed('k'):
        steer = 40
    elif keyboard.is_pressed('l'):
        steer = -40 
    else:
        steer = 0

    if keyboard.is_pressed('f'): 
        motor.test(0,1,pwm)
        break

    # print(speed)
    camera.capture('/home/pi/neuroDrive/images/' + str(index) + ".jpg", use_video_port = True)
    if (steer == 40):
        temp.append("l")
        print("l")
    elif (steer == -40):
        temp.append("r")
    else:
        temp.append("c")
    motor.steertest(steer, pwm)
    motor.test(speed,1,pwm)

    index = index + 1
    data.append(temp)

with open('data.csv','wb') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    wr.writerows([["image", "steer"]])
    wr.writerows(data)
