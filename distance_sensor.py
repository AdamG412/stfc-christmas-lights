#Simple script to get data from HCSR04 ultrasound distance sensors
import board
import time
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP0, echo_pin=board.GP1)

while True:
    try:
        print(sonar.distance)
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)