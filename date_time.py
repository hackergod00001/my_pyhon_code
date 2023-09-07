from pytz import timezone
from datetime import datetime  # imported module datetime
now = datetime.now()  # here nw on the lhs is an object
print("Now:", now)
print("Today's date: ", now.strftime('%Y-%m-%d'))
print("Today's date: ", now.strftime('%d-%m-%Y'))

print("Year:", now.year)
print("month:", now.month)
print("day:", now.day)
print("hour:", now.hour)
print("minute:", now.minute)
print("second:", now.second)

# The strftime() method can be used to create formatted strings.

# %%
# Write a program to demonstrate
# conversion of time across
# various timezones
# current time
print(datetime.now())
# current time to UTC
now_utc = datetime.now(timezone('UTC'))
print(now_utc.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
# current time to US/Eastern
now_useastern = datetime.now(timezone('US/Eastern'))
print(now_useastern.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
# current time to Asia/Kolkata time zone
now_india = datetime.now(timezone('Asia/Kolkata'))
print(now_india.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
# %%
