import datetime
import calendar

def main():
    """
    Examples of additional useful datetime methods and properties.
    """
    print("=== Additional Datetime Methods and Properties ===\n")
    
    # Current date for reference
    today = datetime.date.today()
    now = datetime.datetime.now()
    print(f"Today's date: {today}")
    print(f"Current datetime: {now}\n")
    
    # 1. Calendar methods
    print("1. Calendar methods:")
    # Check if current year is a leap year
    is_leap = calendar.isleap(today.year)
    print(f"   Is {today.year} a leap year? {is_leap}")
    
    # Get calendar for current month
    cal = calendar.monthcalendar(today.year, today.month)
    print(f"   Calendar for {calendar.month_name[today.month]} {today.year}:")
    print("   Mo Tu We Th Fr Sa Su")
    for week in cal:
        week_str = "   "
        for day in week:
            if day == 0:
                week_str += "   "
            else:
                week_str += f"{day:2d} "
        print(week_str)
    
    # 2. Date components and attributes
    print("\n2. Date components and attributes:")
    
    # Using isocalendar() - returns a tuple (ISO year, ISO week number, ISO weekday)
    iso_cal = today.isocalendar()
    print(f"   ISO Year: {iso_cal[0]}, ISO Week: {iso_cal[1]}, ISO Weekday: {iso_cal[2]}")
    
    # For Python 3.9+, isocalendar() returns a named tuple
    try:
        print(f"   ISO Year: {iso_cal.year}, ISO Week: {iso_cal.week}, ISO Weekday: {iso_cal.weekday}")
    except AttributeError:
        print("   Note: In Python 3.9+, isocalendar() returns a named tuple with year, week, and weekday attributes")
    
    # isoweekday() - returns weekday where Monday=1, Sunday=7
    print(f"   ISO Weekday: {today.isoweekday()} (1=Monday, 7=Sunday)")
    
    # timetuple() - returns a time.struct_time object
    time_tuple = today.timetuple()
    print(f"   Time tuple: {time_tuple}")
    print(f"   Day of year from time tuple: {time_tuple.tm_yday}")
    
    # 3. Replacing components with replace()
    print("\n3. Replacing components with replace():")
    
    # Replace year
    next_year = today.replace(year=today.year + 1)
    print(f"   Same day next year: {next_year}")
    
    # Replace multiple components in a datetime
    noon_today = now.replace(hour=12, minute=0, second=0, microsecond=0)
    print(f"   Noon today: {noon_today}")
    
    # Create a date from ordinal (days since 01-01-0001)
    ordinal_date = datetime.date.fromordinal(today.toordinal() + 100)
    print(f"   100 days from today: {ordinal_date}")
    
    # 4. Working with time objects
    print("\n4. Working with time objects:")
    
    # Create a time object
    noon = datetime.time(12, 0, 0)
    print(f"   Noon: {noon}")
    
    # Time components
    print(f"   Hour: {noon.hour}, Minute: {noon.minute}, Second: {noon.second}")
    
    # Time comparison
    time1 = datetime.time(9, 0, 0)
    time2 = datetime.time(17, 0, 0)
    print(f"   {time1} < {time2}: {time1 < time2}")
    
    # 5. Combining date and time
    print("\n5. Combining date and time:")
    
    # combine() - creates a datetime from a date and time
    meeting_date = datetime.date(2023, 10, 15)
    meeting_time = datetime.time(14, 30)
    meeting = datetime.datetime.combine(meeting_date, meeting_time)
    print(f"   Meeting: {meeting}")
    
    # Extract date and time from datetime
    extracted_date = meeting.date()
    extracted_time = meeting.time()
    print(f"   Extracted date: {extracted_date}")
    print(f"   Extracted time: {extracted_time}")
    
    # 6. Working with tzinfo abstract base class
    print("\n6. Working with tzinfo:")
    
    # Create a simple fixed offset timezone class
    class FixedOffset(datetime.tzinfo):
        def __init__(self, offset_hours, name):
            self.__offset = datetime.timedelta(hours=offset_hours)
            self.__name = name
            
        def utcoffset(self, dt):
            return self.__offset
            
        def tzname(self, dt):
            return self.__name
            
        def dst(self, dt):
            return datetime.timedelta(0)
    
    # Create timezone objects
    utc = FixedOffset(0, "UTC")
    ist = FixedOffset(5.5, "IST")
    
    # Create timezone-aware datetime objects
    utc_dt = datetime.datetime.now(utc)
    ist_dt = datetime.datetime.now(ist)
    
    print(f"   UTC time: {utc_dt}")
    print(f"   IST time: {ist_dt}")
    print(f"   UTC offset for IST: {ist.utcoffset(None)}")

if __name__ == "__main__":
    main()
