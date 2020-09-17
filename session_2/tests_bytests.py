import time
a = time.time()
print(a)
print(time.gmtime(a))
"""time.struct_time(tm_year=2020, tm_mon=9, tm_mday=10, tm_hour=15, tm_min=10, tm_sec=4, tm_wday=3, tm_yday=254, tm_isdst=0)"""

c = time.struct_time((2020, 9, 10, 23, 59, 59, 0, 0, 0))
#d = time.gmtime(a)



#day, month, year = [int(i) for i in input().split(".")]
#b = (year, month, day, 23, 59, 59, 0, 0, 0)
print(time.mktime(c))
#print(time.mktime(d))
#print(time.mktime(b))
#print(time.mktime(a))

import time


def get_seconds(day, month, year):
    return time.mktime((year, month, day, 23, 59, 59, 0, 0, 0))


print(get_seconds(10, 9, 2020))


