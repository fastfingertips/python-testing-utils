import re

def main():
    """
    Basic data extraction examples.
    """
    print("=== Basic Data Extraction Examples ===\n")
    
    # Sample text
    text = """
    Personal Information:
    Name: John Smith
    Email: john.smith@example.com
    Phone: +1 555 123 4567
    Birth Date: 04/15/1985
    Address: 123 Main St, New York, NY 10001
    """
    print(f"Sample text: \n{text}")
    
    # 1. Extract name
    name_pattern = r"Name: (.+)"
    name_match = re.search(name_pattern, text)
    if name_match:
        print(f"1. Name: {name_match.group(1)}")
    
    # 2. Extract email
    email_pattern = r"Email: ([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})"
    email_match = re.search(email_pattern, text)
    if email_match:
        print(f"2. Email: {email_match.group(1)}")
    
    # 3. Extract phone number
    phone_pattern = r"Phone: (\+\d+\s\d+\s\d+\s\d+)"
    phone_match = re.search(phone_pattern, text)
    if phone_match:
        print(f"3. Phone: {phone_match.group(1)}")
    
    # 4. Extract birth date
    birthdate_pattern = r"Birth Date: (\d{2}/\d{2}/\d{4})"
    birthdate_match = re.search(birthdate_pattern, text)
    if birthdate_match:
        print(f"4. Birth Date: {birthdate_match.group(1)}")
    
    # 5. Extract address
    address_pattern = r"Address: (.+)"
    address_match = re.search(address_pattern, text)
    if address_match:
        print(f"5. Address: {address_match.group(1)}")

if __name__ == "__main__":
    main()
