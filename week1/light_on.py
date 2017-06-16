
import RPi.GPIO as GPIO  # Import GPIO library
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)  # Set the pin numbering
GPIO.setup(26, GPIO.OUT)  # Setup GPIO Pin 26 to OUT

GPIO.output(26, True)  # Turn on GPIO pin 26
time.sleep(1)
GPIO.output(26, False)  # Turn off GPIO pin 26

GPIO.cleanup()
