import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

gpio.setup(23, gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(18, gpio.OUT)

while True:
    buttonPressed = gpio.input(23)
    if buttonPressed == 1:
        gpio.output(18, gpio.LOW)
    if buttonPressed == 0:
        gpio.output(18, gpio.HIGH)

