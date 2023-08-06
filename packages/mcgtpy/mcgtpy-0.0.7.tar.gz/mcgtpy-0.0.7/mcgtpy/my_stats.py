### This is a testing module to make sure things are running smoothly as I setup this function on pip

# Imports
import datetime
import timedelta

### Methods
def print_stats():
    # My Name
    my_name = "Myles Thomas"
    print(f"My name is {my_name}. \n")

    # My Birthday
    my_birthday_date = datetime.date(year=1998, month=2, day=23)
    print(f"My Birthday was on this date: {my_birthday_date}. \n")

    # Current Date
    current_date = datetime.date.today()
    print(f"The current date today is: {current_date}. \n")

    # How long I have been alive
    difference_timedelta = abs(current_date - my_birthday_date)
    time_alive_days_int = difference_timedelta.days
    time_alive_years_int = int(time_alive_days_int / 365) # round down closer to 0 
    print(f"I have been alive for: {time_alive_years_int} years (~{time_alive_days_int} days). \n")

    # Current Age
    current_age_int = int(time_alive_years_int) # round down closer to 0 
    print(f"My current age is {current_age_int}. \n")

    # How many days away I am from my Age + 1 birthday
    next_age_int = current_age_int + 1
    next_birthday_date = datetime.date(year=my_birthday_date.year + next_age_int, month=my_birthday_date.month, day=my_birthday_date.day)
    difference_timedelta = abs(current_date - next_birthday_date)
    days_until_birthday_int = difference_timedelta.days
    print(f"I am {days_until_birthday_int} days away from turning {next_age_int}, which will take place on {next_birthday_date}! \n")

    # End
    print("Until next time! \n")