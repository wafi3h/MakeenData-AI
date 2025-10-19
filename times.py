from datetime import datetime

time_1 = input("Enter the first time: ")
time_2 = input("Enter the second time: ")


time_format = "%H:%M%p"
time1 = datetime.strptime(time_1, time_format).time()
time2 = datetime.strptime(time_2, time_format).time()

if time1 > time2:
    print(time_1," is later than ",time_2)
elif time1 < time2:
    print(time_1,"is earlier than ",time_2)
else:
    print(time_1,"and ",time_2, "are the same.")