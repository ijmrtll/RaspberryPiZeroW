# Write your code here :-)
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

try:
    while True:
        GPIO.output(14, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(14, GPIO.LOW)
        sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()