# Write your code here :-)
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)
pwm = GPIO.PWM(15, 100)
value = 0
pwm.start(value)
increment = 2
sleeptime = 0.03

try:
    while True:
        value += increment
        if value > 50:
            increment = -increment
            value += 2*increment
        elif value <= 0:
            increment = -increment
            value += 2*increment
        pwm.ChangeDutyCycle(value)
        sleep(sleeptime)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()