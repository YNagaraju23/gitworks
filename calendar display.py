#def decorator_function(func):
#    def wrapper():
#        print("first statement")
#        func()
#        print("second statement")
#    return wrapper
#@decorator_function
#def print_sum():
#    print(5+3)
#
#print_sum()

#list1 = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat' ]
#for i,d in enumerate(list1):
#    print(i, d)


#def my_func(greetings):
#    print("Hello, " + greetings)
#    print(name)
#my_func("Good Morning")
#k = "raju"
#print(f'hello {k}')

#import datetime
#now = datetime.datetime.now()
#print ("Current date and time : ", now.strftime("%Y-%m-%d %H:%M:%S"))


#time delta
#from datetime import timedelta
#print(dir(timedelta))

import calendar
yy = 2024
mm = 11
# display the calendar
print(calendar.month(yy, mm))

print("**********************")
c = calendar.TextCalendar(calendar.SUNDAY)
thestr = c.formatmonth(2026, 3)
print(thestr)