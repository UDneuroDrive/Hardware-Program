#run AJmotortimeout.py to use this file
#both files must be in the same folder on the Pi
import time

#servo setup
def setup(pwm):
    #start motor at 0 speed when no connection
    #ticks was 305 for car, changed to 316 for cont. servo
    Ticks = 305
    pwm.set_pwm(1, 0, Ticks)  
   
# Begin Motor Control   
def test(speedpi,StartStop,pwm):
    period = 20
    #print "Speedpi: ", speedpi
    #print "StartStop: ", 
    if StartStop == 0:
        #Setting zero to 1.464 ms or 300 ticks
        #pulselength = 1.325
        #Ticks = int( 1.325 / 0.00488 )
        #ticks was 305 for car, changed to 316 for cont. servo
        Ticks = 305
        pwm.set_pwm(1, 0, Ticks)
        #print "Motor Ticks 1: ", Ticks
        
    else:
        if speedpi < 0: #reverse
            speed = -speedpi
            #Original - pulselength = ((speed*(0.175/50)+1.35))
            #Mine...
            pulselength = (speed*(0.175/50)+1.5)
            #print "Motor Pulselength Reverse: ", pulselength
            Ticks = int( pulselength / 0.00488 )
            pwm.set_pwm(1, 0, Ticks)
            #print "Motor Ticks 2: ", Ticks
        
        elif speedpi > 0: #forward
            #Original - pulselength = (speedpi*(0.30/100)-1.3)*-1
            pulselength = (speedpi*(0.30/100)-1.5)*-1
            #print "Motor Pulselength Forward: ", pulselength
            Ticks = int( pulselength / 0.00488 )
            pwm.set_pwm(1, 0, Ticks)
            #print "Motor Ticks 3: ", Ticks
            
        else: #all other values
            #Needs to be set to around 1.5 ms or 300-310 Ticks
            #pulselength = 1.325
            #Ticks = int( 1.325 / 0.00488 )
            #ticks was 305 for car, changed to 316 for cont. servo
            Ticks = 305
            pwm.set_pwm(1, 0, Ticks)
            #print "Motor Ticks 4: ", Ticks
            
#set motor to 0 speed in the event of a timeout
def timeout(pwm):
    print 'Lost connection!'
    #ticks was 305 for car, changed to 316 for cont. servo
    Ticks = 305
    pwm.set_pwm(1, 0, Ticks) 
    #period = 20
    #pulselength = 1.325   
#End Motor Control
       
def steertest(steerpi, pwm):
    # Set freq to 50 Hz
    # Steering angles examples
    # For a 60 degree span
    # pulselength = float((steering * (.0055555556))+1.33335)
    # Ticks = integer( pulsewidth / length of one tick )

    steering = steerpi + 40
    #Next line is new for 
    Ticks = int(float((2.3 * steering * (.0041666667))+1.23335) / (0.00488))
    #Ticks = int(float((2.3 * steering * (.0055555556))+1.23335) / (0.00488))
    pwm.set_pwm(15, 0, Ticks)
    #print 'Steering Ticks: ', Ticks
 
#End Steering Control
       
def cameraboi(UpDownLevel, LeftRightLevel, pwm):
    #print "UpDownLevel: ", UpDownLevel
    #print "LeftRightLevel: ", LeftRightLevel
    #Setting servo address 4 to Up/Down
    #Setting servo address 6 to Left/Right
    TicksUpDown = int(UpDownLevel / 0.00488)
    TicksLeftRight = int(LeftRightLevel / 0.00488)
    pwm.set_pwm(4, 0, TicksUpDown)
    pwm.set_pwm(6, 0, TicksLeftRight)
       
def close():
    servo.stop()
if __name__=='__main__':
    setup()
