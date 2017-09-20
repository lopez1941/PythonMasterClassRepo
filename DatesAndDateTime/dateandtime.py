# import time
#
# print(" the epoch starts at " + time.strftime('%c', time.gmtime(0)))
#
# print("the current time zone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\tDaylight savings time is in effect for this location.")
#     print("\tThe DST timezone is " + time.tzname[1])
#
# print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

import datetime

time_local = datetime.datetime.now()
print("local time is {}".format(time_local.strftime('%x %X')))
print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())
