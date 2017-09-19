# this is my dictionary of choices
import pytz
import datetime

us_zone_dict = {}
for j in range ( 1, 10 ):
    us_zone = pytz.country_timezones['US'][j]
    us_zone_dict[j] = us_zone
    print("{0}: {1}".format (j, us_zone_dict[j]))
