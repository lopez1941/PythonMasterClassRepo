import time


timeClock = time.get_clock_info("time")
print("The time() clock info is: {0}".format(timeClock))
timePerf = time.get_clock_info("perf_counter")
print("The perf_counter clock info is: {0}".format(timePerf))
timeMono = time.get_clock_info("monotonic")
print("The monotonic clock info is: {0}".format(timeMono))
timeProc = time.get_clock_info("process_time")
print("The process_time clock info is: {0}".format(timeProc))
