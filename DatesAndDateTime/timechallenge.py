# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz

print("Please choose a timezone below to play TimeZone-Inator!")

us_zone_dict = {'1': ("US/Eastern", pytz.timezone('US/Eastern')),
                '2': ("Japan", pytz.timezone('Japan')),
                '3': ("Israel", pytz.timezone('Israel')),
                '4': ("US/Mountain", pytz.timezone('US/Mountain')),
                '5': ("US/Pacific", pytz.timezone('US/Pacific')),
                '6': ("US/Central", pytz.timezone('US/Central')),
                '7': ("Europe/Paris", pytz.timezone('Europe/Paris')),
                '8': ("Europe/London", pytz.timezone('Europe/London')),
                '9': ("Australia/Darwin", pytz.timezone('Australia/Darwin'))}

for key in sorted(us_zone_dict.keys()):
    print(key, us_zone_dict[key][0])

print("Enter 0 to quit!")

user_choice = '1'

while user_choice != '0':
    user_choice = input("What is your choice? ")
    if user_choice in us_zone_dict.keys():
        chosen_zone, py_zone_entry = us_zone_dict[user_choice]

        utc_time_now = datetime.datetime.now(tz=pytz.UTC)
        #local_time_aware = utc_time_now.astimezone(pytz.timezone('US/Eastern'))
        local_time_aware = utc_time_now.astimezone(tz=None)
        user_time_aware = utc_time_now.astimezone(py_zone_entry)

        print("The time in {0} is {1}" \
              .format(chosen_zone, user_time_aware.strftime('%x %X')))
        print("UTC time is {0}".format(utc_time_now.strftime('%x %X')))
        print("Local time is {0}".format(local_time_aware.strftime('%x %X')))
        print("=" * 50)

    elif user_choice == '0':
        print("Sorry you want to quit!")
        break
    else:
        print("Woops, try again!")
