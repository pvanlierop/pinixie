# pinixie
Raspberry Pi Nixie Clock

This is python code running on a Raspberry Pi Zero W to drive 4 IN-11 Nixie tubes.

The nixies are driven direct from the GPIO ports to K155ID1 chips which in turn connect to the nixie tubes.  170V power is supplied to the nixies complements of the Taylor Electronics Services 1363 HVPS.

Some ideas for implementation:

Add RTC
Setup as an AP as well as a WiFi client so that it could be setup on a wifi network via computer/mobile
