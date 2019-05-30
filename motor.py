import RPi.GPIO as GPIO
from time import sleep

def engineStart():
    global pwm1
    global pwm2
    # PIN DUZENI, SIRA SAYISINA GÖRE
    GPIO.setmode(GPIO.BOARD)
    # MOTOR 1
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)
    # MOTOR 2
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)

    pwm1=GPIO.PWM(7, 100)
    pwm2=GPIO.PWM(15, 100)
    pwm1.start(0)
    pwm2.start(0)
    # PWM GÜCÜ %60
    pwm1.ChangeDutyCycle(60)
    pwm2.ChangeDutyCycle(60)

def setSpeed(speed):
    global pwm1
    global pwm2
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)

def engineStop():
    GPIO.output(19,False)
    GPIO.output(21,False)
    GPIO.output(7,False)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,False)
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

def engineWait():
    GPIO.output(19,False)
    GPIO.output(21,False)
    GPIO.output(7,False)
    GPIO.output(11,False)
    GPIO.output(13,False)
    GPIO.output(15,False)

def goForward():
    GPIO.output(19,True)
    GPIO.output(21,False)
    GPIO.output(7,True)

    GPIO.output(11,True)
    GPIO.output(13,False)
    GPIO.output(15,True)

def goBackward():
    GPIO.output(19,False)
    GPIO.output(21,True)
    GPIO.output(7,True)

    GPIO.output(11,False)
    GPIO.output(13,True)
    GPIO.output(15,True)

def turnLeft():
    global pwm1
    global pwm2
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)

    GPIO.output(19,False)
    GPIO.output(21,True)
    GPIO.output(7,True)

    GPIO.output(11,True)
    GPIO.output(13,False)
    GPIO.output(15,True)
    sleep(0.45)
    engineWait()

def turnRight():
    global pwm1
    global pwm2
    pwm1.ChangeDutyCycle(100)
    pwm2.ChangeDutyCycle(100)

    GPIO.output(19,True)
    GPIO.output(21,False)
    GPIO.output(7,True)

    GPIO.output(11,False)
    GPIO.output(13,True)
    GPIO.output(15,True)
    sleep(0.45)
    engineWait()
