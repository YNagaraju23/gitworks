import inspect
from datetime import date
from datetime import datetime
print(dir(date))
print("******************************")
print(date.today())
date=date.today()
print(date.year)
print(date.month)
print(date.day)
Time=datetime.now()
print(Time)
print(Time.hour,":",Time.minute,":",Time.second)
print(Time.tzinfo)

print("*****************************")
date_string = "14-05-2026"

date_obj = datetime.strptime(date_string, "%d-%m-%Y")

print(date_obj)