import datetime

def main():
    """
    Examples of datetime arithmetic operations.
    """
    print("=== Datetime Arithmetic Operations ===\n")
    
    # Current datetime for reference
    now = datetime.datetime.now()
    print(f"Current datetime: {now}\n")
    
    # 1. Adding and subtracting with timedelta
    print("1. Adding and subtracting with timedelta:")
    
    # Create a timedelta
    one_day = datetime.timedelta(days=1)
    one_week = datetime.timedelta(weeks=1)
    one_hour = datetime.timedelta(hours=1)
    complex_delta = datetime.timedelta(days=2, hours=3, minutes=15, seconds=30)
    
    # Add to datetime
    tomorrow = now + one_day
    next_week = now + one_week
    one_hour_later = now + one_hour
    future = now + complex_delta
    
    print(f"   Tomorrow: {tomorrow}")
    print(f"   Next week: {next_week}")
    print(f"   One hour later: {one_hour_later}")
    print(f"   Complex addition: {future}")
    
    # Subtract from datetime
    yesterday = now - one_day
    last_week = now - one_week
    one_hour_ago = now - one_hour
    past = now - complex_delta
    
    print(f"   Yesterday: {yesterday}")
    print(f"   Last week: {last_week}")
    print(f"   One hour ago: {one_hour_ago}")
    print(f"   Complex subtraction: {past}")
    
    # 2. Creating timedeltas
    print("\n2. Creating timedeltas:")
    print(f"   One day: {datetime.timedelta(days=1)}")
    print(f"   One week: {datetime.timedelta(weeks=1)}")
    print(f"   One hour: {datetime.timedelta(hours=1)}")
    print(f"   One minute: {datetime.timedelta(minutes=1)}")
    print(f"   One second: {datetime.timedelta(seconds=1)}")
    print(f"   One millisecond: {datetime.timedelta(milliseconds=1)}")
    print(f"   One microsecond: {datetime.timedelta(microseconds=1)}")
    
    # 3. Difference between two dates
    print("\n3. Difference between two dates:")
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 12, 31)
    difference = end_date - start_date
    
    print(f"   Start date: {start_date}")
    print(f"   End date: {end_date}")
    print(f"   Difference: {difference}")
    print(f"   Total days: {difference.days}")
    print(f"   Total seconds: {difference.total_seconds()}")
    print(f"   Total hours: {difference.total_seconds() / 3600}")
    
    # 4. Working with specific time periods
    print("\n4. Working with specific time periods:")
    
    # First day of current month
    first_day = datetime.datetime(now.year, now.month, 1)
    print(f"   First day of current month: {first_day.date()}")
    
    # Last day of current month
    if now.month == 12:
        next_month = datetime.datetime(now.year + 1, 1, 1)
    else:
        next_month = datetime.datetime(now.year, now.month + 1, 1)
    
    last_day = next_month - datetime.timedelta(days=1)
    print(f"   Last day of current month: {last_day.date()}")
    
    # First day of current year
    first_day_of_year = datetime.datetime(now.year, 1, 1)
    print(f"   First day of current year: {first_day_of_year.date()}")
    
    # Last day of current year
    last_day_of_year = datetime.datetime(now.year, 12, 31)
    print(f"   Last day of current year: {last_day_of_year.date()}")
    
    # 5. Date comparisons
    print("\n5. Date comparisons:")
    date1 = datetime.datetime(2023, 5, 15)
    date2 = datetime.datetime(2023, 10, 20)
    
    print(f"   date1: {date1}")
    print(f"   date2: {date2}")
    print(f"   date1 < date2: {date1 < date2}")
    print(f"   date1 > date2: {date1 > date2}")
    print(f"   date1 == date2: {date1 == date2}")
    print(f"   date1 != date2: {date1 != date2}")
    
    # 6. Finding weekdays
    print("\n6. Finding weekdays:")
    
    # Find next Monday
    def next_weekday(d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0:  # Target day already happened this week
            days_ahead += 7
        return d + datetime.timedelta(days=days_ahead)
    
    next_monday = next_weekday(now, 0)  # 0 = Monday
    next_friday = next_weekday(now, 4)  # 4 = Friday
    
    print(f"   Next Monday: {next_monday.date()}")
    print(f"   Next Friday: {next_friday.date()}")

if __name__ == "__main__":
    main()
