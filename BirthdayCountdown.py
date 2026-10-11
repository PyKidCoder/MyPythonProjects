import datetime as dt


print("-----------------------------------")
print(" WELCOME TO THE BIRTHDAY COUNTDOWN")
print("-----------------------------------")

print("I can find out how many days hours, minutes, seconds are left for you birthday")
print("So lets start")

year = int(input("Which year were born in\n"))
month = int(input("Which Month , 1 for Jan , 2 for Feb and so on\n"))
date = int(input("Which day in th month\n"))

date_time = dt.datetime (year , month , date)

weekday_names = ["Monday" "Tuesday" "Wednesday" "Thusday" "Friday" "Saturday" "Sunday"]
weekday_num = date_time . weekday()
print("You Might Have Forgotten")
print("but it was a ") (weekday_names[weekday_num])

current_time = dt.datetime.now()
thisyear = current_time.year
thisyear_bday = dt.datetime(thisyear , month , date)

if thisyear_bday > current_time:
    next_bday = thisyear_bday
else:
    next_bday = dt.datetime(thisyear +1 , month , date)

while next_bday > current_time:
    current_time = dt.datetime.now()
    dd = next_bday - current_time

    days_left = dd.days
    total_seconds_left = dd.seconds

    seconds_left = total_seconds_left % 60
    total_mins_left = total_seconds_left //60
    hrs_left = total_mins_left//60
    mins_left = total_mins_left%60

    print("Your next birthday is", days_left, )