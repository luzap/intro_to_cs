"""Additional challenge: time difference"""
import datetime

# Handling user input
user_day = int(input("Please enter a day: "))
user_month = int(input("Please enter a month: "))
user_year = int(input("Please enter a year: "))

# Date variables
today = datetime.datetime.today().date()
user_date = datetime.datetime(
    year=user_year, month=user_month, day=user_day).date()
time_diff = today - user_date
day_string = "day" + "s" * (time_diff.days > 1 or time_diff.days == 0)

# Output
print("That was {} {} ago.".format(time_diff.days, day_string))
