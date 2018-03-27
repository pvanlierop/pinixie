import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
HIGH = 1
LOW = 0
# setup up constants for GPIO PINS
DIG1_1 = 23
DIG1_2 = 24
DIG1_3 = 25
DIG1_4 = 8
DIG2_1 = 7
DIG2_2 = 12
DIG2_3 = 16
DIG2_4 = 20
DIG3_1 = 21
DIG3_2 = 26
DIG3_3 = 13
DIG3_4 = 6
DIG4_1 = 5
DIG4_2 = 22
DIG4_3 = 27
DIG4_4 = 17
NIX1 = [DIG1_1, DIG1_2, DIG1_3, DIG1_4]
NIX2 = [DIG2_1, DIG2_2, DIG2_3, DIG2_4]
NIX3 = [DIG3_1, DIG3_2, DIG3_3, DIG3_4]
NIX4 = [DIG4_1, DIG4_2, DIG4_3, DIG4_4]
ALL_NIXIES = [NIX1, NIX2, NIX3, NIX4]

#setup binary output for nixie to display for each digit
OUT0 = [0,0,0,0]
OUT1 = [1,0,0,0]
OUT2 = [0,1,0,0]
OUT3 = [1,1,0,0]
OUT4 = [0,0,1,0]
OUT5 = [1,0,1,0]
OUT6 = [0,1,1,0]
OUT7 = [1,1,1,0]
OUT8 = [0,0,0,1]
OUT9 = [1,0,0,1]
ALL_NUMBERS = [OUT0, OUT1, OUT2, OUT3, OUT4, OUT5, OUT6, OUT7, OUT8, OUT9]

GPIO.setup(NIX1, GPIO.OUT)
GPIO.setup(NIX2, GPIO.OUT)
GPIO.setup(NIX3, GPIO.OUT)
GPIO.setup(NIX4, GPIO.OUT)

def cycle_nixies():
    for i in ALL_NIXIES:
        for j in ALL_NUMBERS:
            GPIO.output(i, j)
            time.sleep(.2)

def display_digit(which_digit, digit_value):
    if (0 <= which_digit <= 3) and (0 <= digit_value <= 9):
        GPIO.output(ALL_NIXIES[which_digit], ALL_NUMBERS[digit_value])

cycle_nixies()
display_digit(0, 1)
display_digit(1, 2)
display_digit(2, 3)
display_digit(3, 4)
time.sleep(10)
GPIO.cleanup()
