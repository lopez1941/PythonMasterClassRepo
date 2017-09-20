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

import pytz
import datetime




print("Please choose a timezone below to play TimeZone-Inator!")

# this is my dictionary of choices
us_zone_dict = {1: ("Eastern", "US/Eastern", pytz.timezone('US/Eastern')),
                2: ("Japan", "Japan", pytz.timezone('Japan')),
                3: ("Israel", "Israel", pytz.timezone('Israel')),
                4: ("Mountain","US/Mountain", pytz.timezone('US/Mountain')),
                5: ("Pacific","US/Pacific", pytz.timezone('US/Pacific')),
                6: ("Central","US/Central", pytz.timezone('US/Central')),
                7: ("Paris","Europe/Paris", pytz.timezone('Europe/Paris')),
                8: ("London","Europe/London", pytz.timezone('Europe/London')),
                9: ("Darwin Australia","Australia/Darwin", pytz.timezone('Australia/Darwin'))}

valid_choice = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
user_choice = ''

print("Enter 0 to quit!")
while user_choice != '0':
    user_choice = input("What is your choice? ")
    if user_choice in valid_choice:
        print("good choice!")
        # local_time = datetime.datetime.now()
        # utc_time = datetime.datetime.utcnow()
        # aware_utc_time = pytz.utc.localize(utc_time)
        # print("UTC time {0}, time zone {1}".format(aware_utc_time, aware_utc_time.tzinfo))

        utc_time_now = datetime.datetime.now(tz=pytz.UTC)
        print("Current UTC time is {}.".format(utc_time_now))
        print("Local time is {}.".format(utc_time_now.astimezone(pytz.timezone('US/Eastern'))))
    elif user_choice == '0':
        print("Sorry you want to quit!")
        break

    else:
        print("you're bad at this")


