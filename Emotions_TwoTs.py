#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
#                      TWO-TS
#  Master's degree in Computer Science at the Federal University of ABC;
#  Title of Work: Two-Ts: Reproduction of Facial Expressions in Robotic Head with 3D Technology;
#  Student: Tamires dos Santos;
#  Advisor: Wagner Tanaka Botelho;
#
#  Description: Basic and Universal Emotions of the Two-Ts.
#
#  Main references: https://github.com/adafruit/Adafruit_Python_PCA9685/blob/master/examples/simpletest.py
#
#  Modification Date: 05/13/2021
#######################################################

from __future__ import division
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#### Servomotors/Positions
# Neck
m0 = 0
m1 = 1
m2 = 2
# Jaw
m3 = 3
# Boca
m4 = 4
m5 = 5
# Eyebrows
m6 = 6
m7 = 7
# Eyes
m8 = 8 #left
m9 = 9 #right
# Eyelids
m10 = 10 #left
m11 = 11 #right
# Mouth
m12 = 12 #left
m13 = 13 #right
#################

# Wrist length
minPulse = 650
maxPulse = 2350

def setAngle(angle):
    pulseWidth = 0
    analogValue = 0
    pulseWidth = (angle - 0)*(maxPulse-minPulse)/180 +minPulse
    analogValue = int(float(pulseWidth) / 1000000 * 50 * 4096)
    return analogValue


# Starting position
def startingPosition():
    pwm.set_pwm(m0, 0, setAngle(100))
    pwm.set_pwm(m1, 0, setAngle(50))
    pwm.set_pwm(m2, 0, setAngle(70))
    pwm.set_pwm(m3, 0, setAngle(0))
    pwm.set_pwm(m4, 0, setAngle(100))
    pwm.set_pwm(m5, 0, setAngle(90))
    pwm.set_pwm(m6, 0, setAngle(130))
    pwm.set_pwm(m7, 0, setAngle(50))
    pwm.set_pwm(m8, 0, setAngle(90))
    pwm.set_pwm(m9, 0, setAngle(90))
    pwm.set_pwm(m10, 0, setAngle(20))
    pwm.set_pwm(m11, 0, setAngle(120))
    pwm.set_pwm(m12, 0, setAngle(90))
    pwm.set_pwm(m13, 0, setAngle(180))


startingPosition()
while True:
    print("1 - Happiness")
    print("2 - Fear")
    print("3 - Disgust")
    print("4 - Anger")
    print("5 - Surprise")
    print("6 - Sadness")
    
    option = input()
    time.sleep(5)

    if option == '1': #Happiness
        #AU 12
        pwm.set_pwm(m4, 0, definirAngulo(10))
        pwm.set_pwm(m5, 0, definirAngulo(180))
        
        #AU 6
        pwm.set_pwm(m10, 0, definirAngulo(70))
        pwm.set_pwm(m11, 0, definirAngulo(90))
        
        time.sleep(5)

        #Neutral Servo Position
        startingPosition()
        time.sleep(4)

        
    elif option == '2': #Fear 
        #AU 1
        pwm.set_pwm(m6, 0, definirAngulo(110))
        pwm.set_pwm(m7, 0, definirAngulo(80))

        #AU 2  #conflict with AU 1
        #AU 4 #conflict with AU 1
        #AU 5 #conflict with AU 7

        #AU 7
        pwm.set_pwm(m10, 0, definirAngulo(60))
        pwm.set_pwm(m11, 0, definirAngulo(100))

        #AU 20

        #AU 26
        pwm.set_pwm(m3, 0, definirAngulo(80))

        time.sleep(5)
        
        #Neutral Servo Position
        startingPosition()
        time.sleep(4)


    elif option == '3': #Disgust
        # AU 4
        pwm.set_pwm(m6, 0, definirAngulo(150))
        pwm.set_pwm(m7, 0, definirAngulo(20))

        #AU 15
        pwm.set_pwm(m12, 0, definirAngulo(180))
        pwm.set_pwm(m13, 0, definirAngulo(90))

        time.sleep(5)
        
        #Neutral Servo Position
        startingPosition()
        time.sleep(4)


    elif option == '4': #Anger
        #AU 4
        pwm.set_pwm(m6, 0, definirAngulo(150))
        pwm.set_pwm(m7, 0, definirAngulo(20))

        #AU 5 #conflict with AU 7

        #AU 7
        pwm.set_pwm(m10, 0, definirAngulo(60))
        pwm.set_pwm(m11, 0, definirAngulo(100))

        #AU 23
        pwm.set_pwm(m12, 0, definirAngulo(180))
        pwm.set_pwm(m13, 0, definirAngulo(90))

        time.sleep(5)
        
        #Neutral Servo Position
        startingPosition()
        time.sleep(4)

        
    elif option == '5': #Surprise
        #AU 1
        pwm.set_pwm(m6, 0, definirAngulo(110))
        pwm.set_pwm(m7, 0, definirAngulo(80))

        #AU 2  #conflict with AU 1

        #AU 5
        pwm.set_pwm(m10, 0, definirAngulo(40))
        pwm.set_pwm(m11, 0, definirAngulo(120))
        
        pwm.set_pwm(m3, 0, definirAngulo(50))

        time.sleep(5)
        
        #Neutral Servo Position
        startingPosition()
        time.sleep(4)
    
    
    elif option == '6': #Sadness
        #AU 1
        pwm.set_pwm(m6, 0, definirAngulo(110))
        pwm.set_pwm(m7, 0, definirAngulo(80))

        #AU 4 #conflict with AU 1

        #AU 15
        pwm.set_pwm(m12, 0, definirAngulo(180))
        pwm.set_pwm(m13, 0, definirAngulo(90))

        time.sleep(5)
        
        #Neutral Servo Position
        startingPosition()
        time.sleep(4)
