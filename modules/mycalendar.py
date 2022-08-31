import sys;
locations = sys.path;
print(locations)

for i in locations:
    print(i)

#CTRL + CLICK to go the module definition
import calendar 

leapdays = calendar.leapdays(2000, 2050)
print(leapdays)
isitleap = calendar.isleap(2036)
print(isitleap)

