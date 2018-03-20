import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
HIGH = 1
LOW = 0
PIN1 = 23
PIN2 = 24
PIN3 = 25
PIN4 = 8

# zero out display
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(PIN3, GPIO.OUT)
GPIO.setup(PIN4, GPIO.OUT)

GPIO.output(PIN1, LOW)
GPIO.output(PIN1, LOW)
GPIO.output(PIN1, LOW)
GPIO.output(PIN1, LOW)

# display 1
time.sleep(1)
GPIO.output(PIN1, HIGH)
GPIO.output(PIN2, LOW)
GPIO.output(PIN3, LOW)
GPIO.output(PIN4, LOW)

# display 2
time.sleep(1)
GPIO.output(PIN1, LOW)
GPIO.output(PIN2, HIGH)
GPIO.output(PIN3, LOW)
GPIO.output(PIN4, LOW)

# display 3
time.sleep(1)
GPIO.output(PIN1, HIGH)
GPIO.output(PIN2, HIGH)
GPIO.output(PIN3, LOW)
GPIO.output(PIN4, LOW)

# display 4
time.sleep(1)
GPIO.output(PIN1, LOW)
GPIO.output(PIN2, LOW)
GPIO.output(PIN3, HIGH)
GPIO.output(PIN4, LOW)
