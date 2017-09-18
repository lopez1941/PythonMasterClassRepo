import time

print(" the epoch starts at " + time.strftime('%c', time.gmtime(0)))

print("the current time zone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
    print("\tDaylight savings time is in effect for this location.")