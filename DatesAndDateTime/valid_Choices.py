import pytz
import datetime

# # this is my set to see if a user picked a valid choice.  if their choice isn't in this set, they
# # must choose again
# valid_choice = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
# print(valid_choice)
# user_choice = ''
#
#
# while user_choice != '0':
#     user_choice = input("What is your choice? ")
#     if user_choice in valid_choice:
#         print("good choice!")
#     elif user_choice == '0':
#         print("Sorry you want to quit!")
#         break
#
#     else:
#         print("you're bad at this")


us_zone_dict = {1: ("US/Eastern", pytz.timezone('US/Eastern')),
                2: ("Japan", pytz.timezone('Japan')),
                3: ("Israel", pytz.timezone('Israel')),
                4: ("US/Mountain", pytz.timezone('US/Mountain')),
                5: ("US/Pacific", pytz.timezone('US/Pacific')),
                6: ("US/Central", pytz.timezone('US/Central')),
                7: ("Europe/Paris", pytz.timezone('Europe/Paris')),
                8: ("Europe/London", pytz.timezone('Europe/London')),
                9: ("Australia/Darwin", pytz.timezone('Australia/Darwin'))}
utc_time_now = datetime.datetime.now(tz=pytz.UTC)
# print("Current UTC time is {}.".format(utc_time_now))
# print("Local time is {}.".format(utc_time_now.astimezone(pytz.timezone('US/Eastern'))))
eastern = us_zone_dict[1]
local_time_aware = utc_time_now.astimezone(pytz.timezone('US/Eastern'))
chosen_zone, py_zone_entry = us_zone_dict[1]
print("UTC time is {0}".format(utc_time_now))
print("Local time is {0}".format(local_time_aware))
print("The time in {0} is {1}"\
      .format(chosen_zone, utc_time_now.astimezone(py_zone_entry) ))
