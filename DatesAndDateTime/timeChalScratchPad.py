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
us_zone_dict = {}
for j in range ( 1, 10 ):
    us_zone = pytz.country_timezones['US'][j]
    us_zone_dict[j] = us_zone
    print("{0}: {1}".format (j, us_zone_dict[j]))

valid_choice = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
user_choice = ''

print("Enter 0 to quit!")
while user_choice != '0':
    user_choice = input("What is your choice? ")
    if user_choice in valid_choice:
        print("good choice!")
        local_time = datetime.datetime.now()
        utc_time = datetime.datetime.utcnow()
        aware_utc_time = pytz.utc.localize(utc_time)
        print("UTC time {0}, time zone {1}".format(aware_utc_time, aware_utc_time.tzinfo))
    elif user_choice == '0':
        print("Sorry you want to quit!")
        break

    else:
        print("you're bad at this")


