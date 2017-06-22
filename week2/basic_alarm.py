import datetime
import time

print (str(datetime.datetime.now()))

alarmTime = datetime.datetime.now() + datetime.timedelta(minutes=1)

print (str(alarmTime))

while datetime.datetime.now() < alarmTime:
    time.sleep(1)
    print ("sleep")

print ("Wake Up !")
print ("Wake Up !")
print ("Wake Up !")
