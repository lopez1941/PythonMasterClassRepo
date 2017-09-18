# import time

# print(time.gmtime(0))
# print(time.gmtime())
# print(time.localtime())
#
# print(time.time())

# in practice, you'd use one or the other, this is just to show two methods available
# time_here = time.localtime()
# print(time_here)
# print("year: ", time_here[0], time_here.tm_year)
# print("month: ", time_here[1], time_here.tm_mon)
# print("day: ", time_here[2], time_here.tm_mday)

# from time import time as my_timer  # don't do it like this in production code
# import random
#
# input("Press enter to start: ")
# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# start_time = my_timer()
# input("Press enter to stop: ")
#
# end_time = my_timer()
# print("Started at " + time.strftime("%X", time.localtime(start_time)))  # strftime means string from time
# print("Ended at " + time.strftime("%X", time.localtime(end_time)))
# print("Your reaction time was {0} seconds".format(end_time - start_time))
import time
#from time import perf_counter as my_timer  # most accurate, best one for this 'game'
# from time import monotonic as my_timer  # time can't go backwards
from time import process_time as my_timer  # not really applicable for this, but tells cpu time used processing
import random

input("Press enter to start: ")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop: ")

end_time = my_timer()
print("Started at " + time.strftime("%X", time.localtime(start_time)))  # strftime means string from time
print("Ended at " + time.strftime("%X", time.localtime(end_time)))
print("Your reaction time was {0} seconds".format(end_time - start_time))
