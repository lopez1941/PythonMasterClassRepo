import datetime
import pytz

country = 'Europe/Moscow'

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)

print("The time in moscow is {}".format(local_time))
print("UTC time is {}".format(datetime.datetime.utcnow()))