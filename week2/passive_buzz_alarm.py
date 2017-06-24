import RPi.GPIO as GPIO  # Import GPIO library
import datetime
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
buzzer = GPIO.PWM(26, 0.5)

print (str(datetime.datetime.now()))

alarmTime = datetime.datetime.now() + datetime.timedelta(minutes=1)

print (str(alarmTime))

while datetime.datetime.now() < alarmTime:
    time.sleep(1)
    print ("sleep")

beepCount = 0

while beepCount < 10:
    print ("Wake Up !")
    buzzer.start(1)
    time.sleep(1)
    buzzer.stop()
    time.sleep(0.5)
    beepCount = beepCount + 1

GPIO.cleanup()
