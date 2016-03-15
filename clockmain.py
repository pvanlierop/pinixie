import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
HIGH = 1
LOW = 0

# Number of Nixie Tubes
NIXIECOUNT = 6

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
    for bit in bits:
        if bit:
            GPIO.output(dataBit, HIGH)
        else:
            GPIO.output(dataBit, LOW)
        pulseCLK()
    return

# Takes a list of appropriate nixie individual values and pushes them to shift register
def nixiePush(digits):
    for tube in range(0, NIXIECOUNT):
        bitShift(intToBit(digits[tube]))

    #now you've shifted the bits, send em!
    serLatch()
    return

    # Clear out shift registers
def shiftBlank():
    for x in range(0, NIXIECOUNT*4):
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

    #Lets try a 1101
    GPIO.output(dataBit, HIGH)
    pulseCLK()
    GPIO.output(dataBit, HIGH)
    pulseCLK()
    GPIO.output(dataBit, LOW)
    pulseCLK()
    GPIO.output(dataBit, HIGH)
    pulseCLK()
    serLatch()

    try:
        while True:
            # get the time and put each digit in a list ready for Nixieing!
            dt = list(time.localtime())
            digitList = [dt[3]/10, dt[3]%10, dt[4]/12, dt[4]%10, dt[5]/10, dt[5]%10 ]
            nixiePush(digitList)
            time.sleep(1)

    except KeyboardInterrupt:
        shiftBlank()
        pass
