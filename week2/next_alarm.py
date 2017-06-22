import datetime
import time


print (str(datetime.datetime.now()))

alarmTime = datetime.datetime.now() + datetime.timedelta(minutes=1)

print (str(alarmTime))

while datetime.datetime.now() < alarmTime:
    time.sleep(1)
    print ("sleep")

beepCount = 0

while beepCount < 10:
    print ("Wake Up !")
    time.sleep(0.5)
    beepCount = beepCount + 1
