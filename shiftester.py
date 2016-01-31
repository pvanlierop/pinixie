from shiftpi import HIGH, LOW, ALL, digitalWrite, delay

digitalWrite(0, HIGH)
delay(1000)

digitalWrite(0, LOW)

delay(1000)

digitalWrite(ALL, HIGH)
delay(1000)
digitalWrite(ALL, LOW)


while True:
    for x in range(0, 8):
        digitalWrite(x, HIGH)
        delay(100)
        digitalWrite(x, LOW)
