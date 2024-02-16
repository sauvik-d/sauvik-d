import calendar as cal


def main():
    cal.setfirstweekday(cal.SUNDAY)
    datasets = [cal.day_name, cal.day_abbr, cal.month_name, cal.month_abbr]
    for calendar_data in datasets:
        print(list(calendar_data))

    print(cal.month(2016, 1))
    cal.prmonth(2017, 3, w=5)


if __name__ == "__main__":
    main()

# time.time() returns the time in seconds since the epoch as a floating point number.
# time.sleep(secs) suspends execution of the program for the given number of seconds.
# time.ctime([secs]) returns a time expressed in seconds since the epoch as a string.
# time.perf_counter() returns the value (in fractional seconds) of a performance counter (i.e. a clock with the highest available resolution to measure a short duration).
# time.process_time() returns the value (in fractional seconds) of the sum of the system and user CPU time of the current process.
# time.strftime(format[,t]) converts a struct_time object t, or the current time if t is not provided, to a string as specified by the format argument.
# time.localtime([secs]) returns an object of type time.struct_time.
# The time.struct_time object is an object with a named tuple interface

