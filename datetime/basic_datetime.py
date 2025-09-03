import datetime

def main():
    """
    Basic examples of creating and using datetime objects.
    """
    print("=== Basic datetime Examples ===\n")
    
    # 1. Get current date
    today = datetime.date.today()
    print(f"1. Current date: {today}")
    print(f"   Year: {today.year}, Month: {today.month}, Day: {today.day}")
    
    # 2. Get current datetime
    now = datetime.datetime.now()
    print(f"\n2. Current datetime: {now}")
    print(f"   Year: {now.year}, Month: {now.month}, Day: {now.day}")
    print(f"   Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}, Microsecond: {now.microsecond}")
    
    # 3. Create a specific date
    specific_date = datetime.date(2023, 12, 31)
    print(f"\n3. Specific date: {specific_date}")
    
    # 4. Create a specific datetime
    specific_datetime = datetime.datetime(2023, 12, 31, 23, 59, 59, 999999)
    print(f"\n4. Specific datetime: {specific_datetime}")
    
    # 5. Get current time
    current_time = datetime.datetime.now().time()
    print(f"\n5. Current time: {current_time}")
    print(f"   Hour: {current_time.hour}, Minute: {current_time.minute}, Second: {current_time.second}")
    
    # 6. Create a specific time
    specific_time = datetime.time(12, 30, 45)
    print(f"\n6. Specific time: {specific_time}")
    
    # 7. Get weekday (0 = Monday, 6 = Sunday)
    print(f"\n7. Today's weekday: {today.weekday()}")
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(f"   Which is: {weekday_names[today.weekday()]}")
    
    # 8. ISO format
    print(f"\n8. ISO format:")
    print(f"   Date ISO: {today.isoformat()}")
    print(f"   Datetime ISO: {now.isoformat()}")
    
    # 9. Get timestamp (seconds since epoch)
    timestamp = datetime.datetime.now().timestamp()
    print(f"\n9. Current timestamp: {timestamp}")
    
    # 10. Create datetime from timestamp
    dt_from_timestamp = datetime.datetime.fromtimestamp(timestamp)
    print(f"   Datetime from timestamp: {dt_from_timestamp}")

if __name__ == "__main__":
    main()
