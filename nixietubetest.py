import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
HIGH = 1
LOW = 0


# Define pins
dataBit = 25
LATCH = 24
CLK = 23

'''
A lot going on in this one. Take an integer and make a 4 bit nibble out of it
instead of using the bin() function we're using format to turn it into a 4 bit
nibble with leading 0 bits if necessary, bin() doesn't do that, we then use 2: to
strip off the 0x into our list
'''
def intToBit(n):
    return [int(digit) for digit in format(n, '#06b')[2:]]

#pulse the shift register clock
def pulseCLK():
    GPIO.output(CLK, HIGH)
    GPIO.output(CLK, LOW)
    return

#latch the shiftregister
def serLatch():
    GPIO.output(LATCH, HIGH)
    GPIO.output(LATCH, LOW)
    return

def bitShift(bits):
    #loop through the bits and shift
    print('Shifting ' + str(bits))
    for bit in bits:
        print ('bit ' + str(bit))
        if bit:
            GPIO.output(dataBit, HIGH)
            print('HIGH')
        else:
            GPIO.output(dataBit, LOW)
            print('LOW')
        pulseCLK()
    return

# cycle through all digits in 10 seconds

def nixieCycle():
    for digit in range(0,9):
        bitShift(intToBit(digit))
        serLatch()
        time.sleep(5)
    return

# Clear out shift registers
def shiftBlank():
    for x in range(0, 4):
        GPIO.output(dataBit, LOW)
        pulseCLK()
    serLatch()
    return

if __name__ == '__main__':

    GPIO.setup(LATCH, GPIO.OUT) # P0
    GPIO.setup(CLK, GPIO.OUT) # P1
    GPIO.setup(dataBit, GPIO.OUT) # P7

    GPIO.output(LATCH, LOW)
    GPIO.output(CLK, LOW)

    # lets clear the register!
    shiftBlank()

    #cycle
    nixieCycle()
