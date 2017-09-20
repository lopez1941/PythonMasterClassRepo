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


# choice = 1
# if choice in us_zone_dict.keys():
#     print(choice, us_zone_dict[choice][0])
user_choice = '1'
print("Enter 0 to quit!")
while user_choice != '0':
    user_choice = input("What is your choice? ")
    if user_choice in us_zone_dict.keys():
        utc_time_now = datetime.datetime.now(tz=pytz.UTC)
        local_time_aware = utc_time_now.astimezone(pytz.timezone('US/Eastern'))
        chosen_zone, py_zone_entry = us_zone_dict[user_choice]
        print("The time in {0} is {1}" \
              .format(chosen_zone, utc_time_now.astimezone(py_zone_entry)))
        print("UTC time is {0}".format(utc_time_now))
        print("Local time is {0}".format(local_time_aware))

    elif user_choice == '0':
        print("Sorry you want to quit!")
        break
    else:
        print("Woops, try again!")