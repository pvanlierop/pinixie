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

# Takes a 24 bit or less variable and outputs the appropriate nixie digits
def nixiePush(bits):

if __name__ == '__main__':

    GPIO.setup(LATCH, GPIO.OUT) # P0
    GPIO.setup(CLK, GPIO.OUT) # P1
    GPIO.setup(dataBit, GPIO.OUT) # P7

    GPIO.output(LATCH, LOW)
    GPIO.output(CLK, LOW)

    # lets clear the register!
    for x in range(0,8):
        GPIO.output(dataBit, LOW)
        pulseCLK()
    serLatch()

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

    dt = list(time.localtime())
    hourDigit1 = dt[3]/10
    hourDigit2 = dt[3]%10
    minDigit1 = dt[4]/10
    minDigit2 = dt[4]%10
    secDigit1 = dt[5]/10
    secDigit2 = dt[5]%10
