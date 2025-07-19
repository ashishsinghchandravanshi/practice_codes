import pandas as pd
#current date and time
print("current date and time",pd.Timestamp.now())

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
day = int(input("Enter day: "))
hour=int(input("enter hour(0-23): "))
#Display the date
timestamp=pd.Timestamp(year=year,month=month,day=day,hour=0)
print(timestamp)

#Display day of week(number)
print("Display day of week: ",timestamp.dayofweek)

#Display day of week(name)
print("Day name: ",timestamp.day_name())

#Display day of year
print("day of the year is: ",timestamp.dayofyear)

#for check leap year
print("leap year: ",timestamp.is_leap_year)

#check if the date is the end of the month
print("is this last day of month ?",timestamp.is_month_end)

#check if the date is the first day of month
print("is this first day of month?: ",timestamp.is_month_start)

#check if the date is last day of the year
print("is this the last day of year: ",timestamp.is_year_end)

#check if the date is first day of the year
print("is this the first day of year: ",timestamp.is_year_start)



