from shiftpi import HIGH, LOW, ALL, digitalWrite, delay

digitalWrite(1, HIGH)
delay(1000)

digitalWrite(1, LOW)

delay(1000)

digitalWrite(ALL, HIGH)
delay(1000)
digitalWrite(ALL, LOW)


while True:
    for x in range(1, 8):
        digitalWrite(x, HIGH)
        delay(2000)
        digitalWrite(x, LOW)
