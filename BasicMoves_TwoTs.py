#!/usr/bin/python
# -*- coding: UTF-8 -*-

#######################################################
#                      TWO-TS
#  Master's degree in Computer Science at the Federal University of ABC;
#  Title of Work: Two-Ts: Reproduction of Facial Expressions in Robotic Head with 3D Technology;
#  Student: Tamires dos Santos;
#  Advisor: Wagner Tanaka Botelho;
#
#  Description: Basic movements of the Two-Ts.
#
#  Main references: https://github.com/adafruit/Adafruit_Python_PCA9685/blob/master/examples/simpletest.py
#
#  Modification Date: 05/12/2021
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


while True:
    print("1 - Head up")
    print("2 - Head down")
    print("3 - head to left")
    print("4 - head to right")
    print("5 - Head rotation to the right")
    print("6 - Head rotation to the left")
    print("7 - Jaw")
    print("8 - Smile")
    print("9 - Left eyebrow")
    print("10 - Right eyebrow")
    print("11 - Eyes to the left")
    print("12 - Eyes to the right")
    print("13 - Blink the left eye")
    print("14 - Blink the right eye")
    print("15 - Smile down")
    
    option = input()
    time.sleep(2)

    if option == '1':
        pwm.set_pwm(m1, 0, setAngle(50))
        pwm.set_pwm(m2, 0, setAngle(70))
        time.sleep(1)
        pwm.set_pwm(m1, 0, setAngle(10))
        pwm.set_pwm(m2, 0, setAngle(120))
        time.sleep(1)
        pwm.set_pwm(m1, 0, setAngle(50))
        pwm.set_pwm(m2, 0, setAngle(70))
        time.sleep(1)

    elif option == '2':
        pwm.set_pwm(m1, 0, setAngle(50))
        pwm.set_pwm(m2, 0, setAngle(70))
        time.sleep(1)
        pwm.set_pwm(m1, 0, setAngle(90))
        pwm.set_pwm(m2, 0, setAngle(20))
        time.sleep(1)
        pwm.set_pwm(m1, 0, setAngle(50))
        pwm.set_pwm(m2, 0, setAngle(70))
        time.sleep(1)

    elif option == '3':
        pwm.set_pwm(m1, 0, setAngle(50))
        pwm.set_pwm(m2, 0, setAngle(70))
        time.sleep(1)
        pwm.set_pwm(m1, 0, setAngle(10))
        pwm.set_pwm(m2, 0, setAngle(20))
        time.sleep(1)
        pwm.set_pwm(m1, 0, setAngle(50))
        pwm.set_pwm(m2, 0, setAngle(70))
        time.sleep(1)

    elif option == '4':
        pwm.set_pwm(m1, 0, setAngle(50))
        pwm.set_pwm(m2, 0, setAngle(70))
        time.sleep(1)
        pwm.set_pwm(m1, 0, setAngle(100))
        pwm.set_pwm(m2, 0, setAngle(120))
        time.sleep(1)
        pwm.set_pwm(m1, 0, setAngle(50))
        pwm.set_pwm(m2, 0, setAngle(70))
        time.sleep(1)

    elif option == '5':
        pwm.set_pwm(m0, 0, setAngle(100))
        time.sleep(1)
        pwm.set_pwm(m0, 0, setAngle(70))
        time.sleep(1)
        pwm.set_pwm(m0, 0, setAngle(100))
        time.sleep(1)

    elif option == '6':
        pwm.set_pwm(m0, 0, setAngle(100))
        time.sleep(1)
        pwm.set_pwm(m0, 0, setAngle(130))
        time.sleep(1)
        pwm.set_pwm(m0, 0, setAngle(100))
        time.sleep(1)
        
    elif option == '7':
        pwm.set_pwm(m3, 0, setAngle(0))
        time.sleep(1)
        pwm.set_pwm(m3, 0, setAngle(90))
        time.sleep(1)
        pwm.set_pwm(m3, 0, setAngle(0))
        time.sleep(1)
        
    elif option == '8':
        pwm.set_pwm(m4, 0, setAngle(100))
        pwm.set_pwm(m5, 0, setAngle(90))
        time.sleep(1)
        pwm.set_pwm(m4, 0, setAngle(10))
        pwm.set_pwm(m5, 0, setAngle(180))
        time.sleep(1)
        pwm.set_pwm(m4, 0, setAngle(100))
        pwm.set_pwm(m5, 0, setAngle(90))
        time.sleep(1)
        
    elif option == '9':
        pwm.set_pwm(m6, 0, setAngle(130))
        time.sleep(1)
        pwm.set_pwm(m6, 0, setAngle(110))
        time.sleep(1)
        pwm.set_pwm(m6, 0, setAngle(130))
        time.sleep(1)
        pwm.set_pwm(m6, 0, setAngle(150))
        time.sleep(1)
        pwm.set_pwm(m6, 0, setAngle(130))
        time.sleep(1)
        
    elif option == '10':
        pwm.set_pwm(m7, 0, setAngle(50))
        time.sleep(1)
        pwm.set_pwm(m7, 0, setAngle(80))
        time.sleep(1)
        pwm.set_pwm(m7, 0, setAngle(50))
        time.sleep(1)
        pwm.set_pwm(m7, 0, setAngle(20))
        time.sleep(1)
        pwm.set_pwm(m7, 0, setAngle(50))
        time.sleep(1)
        
    elif option == '11':
        pwm.set_pwm(m8, 0, setAngle(90))
        pwm.set_pwm(m9, 0, setAngle(90))
        time.sleep(1)
        pwm.set_pwm(m8, 0, setAngle(60))
        pwm.set_pwm(m9, 0, setAngle(60))
        time.sleep(1)
        pwm.set_pwm(m8, 0, setAngle(90))
        pwm.set_pwm(m9, 0, setAngle(90))
        time.sleep(1)
        
    elif option == '12':
        pwm.set_pwm(m8, 0, setAngle(90))
        pwm.set_pwm(m9, 0, setAngle(90))
        time.sleep(1)
        pwm.set_pwm(m8, 0, setAngle(120))
        pwm.set_pwm(m9, 0, setAngle(120))
        time.sleep(1)
        pwm.set_pwm(m8, 0, setAngle(90))
        pwm.set_pwm(m9, 0, setAngle(90))
        time.sleep(1)
        
    elif option == '13':
        pwm.set_pwm(m10, 0, setAngle(20))
        time.sleep(1)
        pwm.set_pwm(m10, 0, setAngle(100))
        time.sleep(1)
        pwm.set_pwm(m10, 0, setAngle(20))
        time.sleep(1)
    
    elif option == '14':
        pwm.set_pwm(m11, 0, setAngle(120))
        time.sleep(1)
        pwm.set_pwm(m11, 0, setAngle(70))
        time.sleep(1)
        pwm.set_pwm(m11, 0, setAngle(120))
        time.sleep(1)
    
    elif option == '15':
        pwm.set_pwm(m12, 0, setAngle(90))
        pwm.set_pwm(m13, 0, setAngle(180))
        time.sleep(1)
        pwm.set_pwm(m12, 0, setAngle(180))
        pwm.set_pwm(m13, 0, setAngle(90))
        time.sleep(1)
        pwm.set_pwm(m12, 0, setAngle(90))
        pwm.set_pwm(m13, 0, setAngle(180))
        time.sleep(1)
        
