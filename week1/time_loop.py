import time

try:
    while True:

        print "Hello World"
        time.sleep(1)

except KeyboardInterrupt:
    print "Bye Bye"

finally:
    print "done"
