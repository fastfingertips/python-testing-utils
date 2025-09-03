import datetime
import zoneinfo  # Python 3.9+ standard library

def main():
    """
    Examples of handling timezones with datetime using only standard library.
    Note: For Python 3.9+, zoneinfo is part of the standard library.
    For earlier versions, use the backport: pip install backports.zoneinfo
    """
    print("=== Timezone Handling Examples ===\n")
    
    # 1. Working with UTC
    print("1. Working with UTC:")
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    print(f"   Current UTC time: {now_utc}")
    
    # Create a UTC datetime using timezone object
    specific_utc = datetime.datetime(2023, 9, 15, 12, 0, 0, tzinfo=datetime.timezone.utc)
    print(f"   Specific UTC time: {specific_utc}")
    
    # 2. Working with timezone offsets
    print("\n2. Working with timezone offsets:")
    
    # Create timezone objects with specific offsets
    utc_plus_3 = datetime.timezone(datetime.timedelta(hours=3))
    utc_minus_5 = datetime.timezone(datetime.timedelta(hours=-5))
    
    # Create datetime objects with specific timezones
    dt_plus_3 = datetime.datetime(2023, 9, 15, 12, 0, 0, tzinfo=utc_plus_3)
    dt_minus_5 = datetime.datetime(2023, 9, 15, 12, 0, 0, tzinfo=utc_minus_5)
    
    print(f"   UTC+3: {dt_plus_3}")
    print(f"   UTC-5: {dt_minus_5}")
    
    # 3. Converting between timezones using zoneinfo (Python 3.9+)
    print("\n3. Converting between timezones using zoneinfo:")
    
    try:
        # Get current time in UTC
        utc_now = datetime.datetime.now(datetime.timezone.utc)
        print(f"   Current UTC time: {utc_now}")
        
        # Convert to different timezones
        timezones = [
            "America/New_York",
            "Europe/London",
            "Asia/Tokyo",
            "Australia/Sydney",
            "Europe/Paris"
        ]
        
        for tz_name in timezones:
            try:
                tz = zoneinfo.ZoneInfo(tz_name)
                local_time = utc_now.astimezone(tz)
                print(f"   {tz_name}: {local_time}")
            except zoneinfo.ZoneInfoNotFoundError:
                print(f"   {tz_name}: Timezone not found")
        
        # 4. Creating aware datetime objects
        print("\n4. Creating aware datetime objects:")
        
        # Create a naive datetime (no timezone info)
        naive = datetime.datetime(2023, 9, 15, 12, 0, 0)
        print(f"   Naive datetime: {naive}")
        
        # Make it timezone-aware with a specific timezone
        try:
            eastern = zoneinfo.ZoneInfo("America/New_York")
            aware_eastern = naive.replace(tzinfo=eastern)
            print(f"   Eastern time: {aware_eastern}")
            
            # Convert to different timezone
            pacific = zoneinfo.ZoneInfo("America/Los_Angeles")
            aware_pacific = aware_eastern.astimezone(pacific)
            print(f"   Pacific time: {aware_pacific}")
        except zoneinfo.ZoneInfoNotFoundError:
            print("   Timezone not found")
        
        # 5. Working with DST (Daylight Saving Time)
        print("\n5. Working with DST (Daylight Saving Time):")
        
        try:
            # Create dates in winter and summer
            winter_date = datetime.datetime(2023, 1, 15, 12, 0, 0)
            summer_date = datetime.datetime(2023, 7, 15, 12, 0, 0)
            
            # Add timezone info
            berlin_tz = zoneinfo.ZoneInfo("Europe/Berlin")
            winter_berlin = winter_date.replace(tzinfo=berlin_tz)
            summer_berlin = summer_date.replace(tzinfo=berlin_tz)
            
            print(f"   Winter in Berlin: {winter_berlin}")
            print(f"   Summer in Berlin: {summer_berlin}")
            print(f"   Winter UTC offset: {winter_berlin.utcoffset()}")
            print(f"   Summer UTC offset: {summer_berlin.utcoffset()}")
        except zoneinfo.ZoneInfoNotFoundError:
            print("   Europe/Berlin timezone not found")
        
        # 6. Available timezones
        print("\n6. Available timezones:")
        print("   To list all available timezones, use:")
        print("   import zoneinfo")
        print("   print(zoneinfo.available_timezones())")
        print("   Note: This returns a large set of timezone names")
    
    except (ImportError, AttributeError):
        print("\nNote: The zoneinfo module requires Python 3.9+")
        print("For earlier versions, use: pip install backports.zoneinfo")

if __name__ == "__main__":
    main()