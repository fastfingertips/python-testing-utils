import re

def main():
    """
    Text substitution examples using groups and backreferences.
    """
    print("=== Text Substitution with Groups and Backreferences ===\n")
    
    # 1. Capturing groups and rearranging
    dates = "Dates: 2023-04-15, 2022-12-31, 2024-01-01"
    print(f"Original dates: {dates}")
    
    # Convert YYYY-MM-DD format to DD/MM/YYYY
    new_dates = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", dates)
    print(f"1. Date format conversion (YYYY-MM-DD -> DD/MM/YYYY): \n   {new_dates}")
    
    # 2. Rearranging names
    names = "John Smith, Jane Doe, Bob Johnson"
    print(f"\nOriginal names: {names}")
    
    # Convert "FirstName LastName" format to "LastName, FirstName"
    new_names = re.sub(r"(\w+)\s+(\w+)", r"\2, \1", names)
    print(f"2. Name format conversion (FirstName LastName -> LastName, FirstName): \n   {new_names}")
    
    # 3. Using named groups
    html = "<div>Content</div>"
    print(f"\nOriginal HTML: {html}")
    
    # Replace HTML tags with markdown using named groups
    new_html = re.sub(r"<(?P<tag>\w+)>(?P<content>.*?)</(?P=tag)>", r"**\g<content>**", html)
    print(f"3. HTML to markdown using named groups: \n   {new_html}")

if __name__ == "__main__":
    main()
