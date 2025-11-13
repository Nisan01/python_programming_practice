#greeting program using time module

import time

time_data=time.strftime('%H:%M:%S')

print(time_data)

time_data=int(time.strftime('%H'))

if time_data <= 12 :
    print("Good Morning")
elif time_data > 12 and time_data < 4 :
    print("Good Afternoon")
else:
    print("Good Evening")    
