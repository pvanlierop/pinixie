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


def cycle_nixies():
    for i in ALL_NIXIES:
        for j in ALL_NUMBERS:
            GPIO.output(i, j)
            time.sleep(.2)

def display_digit(which_digit, digit_value):
    GPIO.output(ALL_NIXIES[which_digit], ALL_NUMBERS[digit_value])

def display_time():
    current_time = list(time.strftime("%I%M"))
    for i in range(0, 4):
        display_digit(i, int(current_time[i]))

if __name__ == '__main__':
    # initialize outputs
    GPIO.setup(NIX1, GPIO.OUT)
    GPIO.setup(NIX2, GPIO.OUT)
    GPIO.setup(NIX3, GPIO.OUT)
    GPIO.setup(NIX4, GPIO.OUT)



    try:
        cycle_nixies()
        second_count = 0
        while True:
            display_time()
            second_count += 1
            if second_count == 3600:
                cycle_nixies()
                second_count = 0
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        pass
