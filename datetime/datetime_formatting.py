import datetime

def main():
    """
    Examples of formatting datetime objects.
    """
    print("=== Datetime Formatting Examples ===\n")
    
    # Sample datetime
    dt = datetime.datetime(2023, 9, 15, 14, 30, 45)
    print(f"Sample datetime: {dt}\n")
    
    # 1. Basic string formatting with strftime()
    print("1. Basic string formatting with strftime():")
    print(f"   Default string: {dt}")
    print(f"   Custom format: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 2. Date formatting
    print("\n2. Date formatting:")
    print(f"   Year: {dt.strftime('%Y')}")  # 4-digit year
    print(f"   Short year: {dt.strftime('%y')}")  # 2-digit year
    print(f"   Month (number): {dt.strftime('%m')}")  # Month as a number (01-12)
    print(f"   Month (name): {dt.strftime('%B')}")  # Full month name
    print(f"   Month (abbr): {dt.strftime('%b')}")  # Abbreviated month name
    print(f"   Day of month: {dt.strftime('%d')}")  # Day of the month (01-31)
    print(f"   Weekday (name): {dt.strftime('%A')}")  # Full weekday name
    print(f"   Weekday (abbr): {dt.strftime('%a')}")  # Abbreviated weekday name
    print(f"   Day of year: {dt.strftime('%j')}")  # Day of the year (001-366)
    
    # 3. Time formatting
    print("\n3. Time formatting:")
    print(f"   Hour (24h): {dt.strftime('%H')}")  # Hour (00-23)
    print(f"   Hour (12h): {dt.strftime('%I')}")  # Hour (01-12)
    print(f"   AM/PM: {dt.strftime('%p')}")  # AM/PM
    print(f"   Minute: {dt.strftime('%M')}")  # Minute (00-59)
    print(f"   Second: {dt.strftime('%S')}")  # Second (00-59)
    print(f"   Microsecond: {dt.strftime('%f')}")  # Microsecond (000000-999999)
    
    # 4. Common date formats
    print("\n4. Common date formats:")
    print(f"   ISO format: {dt.strftime('%Y-%m-%d')}")  # ISO format (YYYY-MM-DD)
    print(f"   US format: {dt.strftime('%m/%d/%Y')}")  # US format (MM/DD/YYYY)
    print(f"   EU format: {dt.strftime('%d/%m/%Y')}")  # European format (DD/MM/YYYY)
    print(f"   Long format: {dt.strftime('%B %d, %Y')}")  # Long format (Month DD, YYYY)
    
    # 5. Common time formats
    print("\n5. Common time formats:")
    print(f"   24-hour: {dt.strftime('%H:%M:%S')}")  # 24-hour format (HH:MM:SS)
    print(f"   12-hour: {dt.strftime('%I:%M:%S %p')}")  # 12-hour format (HH:MM:SS AM/PM)
    print(f"   Time with milliseconds: {dt.strftime('%H:%M:%S.%f')[:-3]}")  # With milliseconds
    
    # 6. Combined date and time formats
    print("\n6. Combined date and time formats:")
    print(f"   ISO datetime: {dt.strftime('%Y-%m-%dT%H:%M:%S')}")  # ISO datetime format
    print(f"   US datetime: {dt.strftime('%m/%d/%Y %I:%M %p')}")  # US datetime format
    print(f"   Custom format: {dt.strftime('%a, %b %d, %Y at %I:%M %p')}")  # Custom format
    
    # 7. Parsing strings to datetime objects with strptime()
    print("\n7. Parsing strings to datetime objects with strptime():")
    date_string = "2023-09-15 14:30:45"
    parsed_dt = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    print(f"   Original string: {date_string}")
    print(f"   Parsed datetime: {parsed_dt}")
    
    # 8. More parsing examples
    print("\n8. More parsing examples:")
    examples = [
        ("September 15, 2023", "%B %d, %Y"),
        ("9/15/23", "%m/%d/%y"),
        ("15-Sep-2023", "%d-%b-%Y"),
        ("Fri, 15 Sep 2023 14:30:45", "%a, %d %b %Y %H:%M:%S")
    ]
    
    for date_str, fmt in examples:
        try:
            parsed = datetime.datetime.strptime(date_str, fmt)
            print(f"   '{date_str}' → {parsed}")
        except ValueError as e:
            print(f"   Error parsing '{date_str}': {e}")

if __name__ == "__main__":
    main()
