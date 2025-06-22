# coverting day and month to string

import datetime

x=datetime.datetime.now()
print("Current date and time is : ",x)

print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%b"))
print(x.strftime("%B"))