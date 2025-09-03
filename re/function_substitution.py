import re

def main():
    """
    Complex text substitution examples using functions.
    """
    print("=== Text Substitution with Functions ===\n")
    
    # Example 1: Double numbers
    def double_number(match):
        number = int(match.group(0))
        return str(number * 2)
    
    text_with_numbers = "Values: 10, 25, 50, 100"
    print(f"Original values: {text_with_numbers}")
    
    new_text = re.sub(r"\d+", double_number, text_with_numbers)
    print(f"1. Doubling numbers: \n   {new_text}")
    
    # Example 2: Toggle case of words
    def toggle_case(match):
        word = match.group(0)
        if word.islower():
            return word.upper()
        else:
            return word.lower()
    
    text_with_mixed_case = "Python with Regex is VERY Useful"
    print(f"\nOriginal text: {text_with_mixed_case}")
    
    new_text = re.sub(r"\b\w+\b", toggle_case, text_with_mixed_case)
    print(f"2. Toggling case of words: \n   {new_text}")
    
    # Example 3: Mask email addresses
    def mask_email(match):
        email = match.group(0)
        username, domain = email.split('@')
        masked_username = username[0] + "*" * (len(username) - 2) + username[-1]
        return f"{masked_username}@{domain}"
    
    text_with_emails = "Contact: john.doe@example.com or jane.smith@company.org"
    print(f"\nOriginal emails: {text_with_emails}")
    
    new_text = re.sub(r"\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}\b", mask_email, text_with_emails)
    print(f"3. Masking email addresses: \n   {new_text}")

if __name__ == "__main__":
    main()
