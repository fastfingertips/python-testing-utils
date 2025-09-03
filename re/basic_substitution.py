import re

def main():
    """
    Basic text substitution examples using re.sub().
    """
    print("=== Basic Text Substitution Examples ===\n")
    
    # Sample text
    text = "Python programming language is useful. Python can be used for web development."
    print(f"Original text: {text}\n")
    
    # 1. Simple word replacement
    new_text = re.sub(r"Python", "JavaScript", text)
    print(f"1. 'Python' -> 'JavaScript': \n   {new_text}")
    
    # 2. Replace only first occurrence (count parameter)
    new_text = re.sub(r"Python", "JavaScript", text, count=1)
    print(f"2. Only first 'Python' -> 'JavaScript': \n   {new_text}")
    
    # 3. Word boundary replacement
    text_with_substring = "Python and Pythonic coding techniques"
    new_text = re.sub(r"\bPython\b", "JavaScript", text_with_substring)
    print(f"3. Word boundary replacement: \n   Original: {text_with_substring} \n   Modified: {new_text}")
    
    # 4. Replace multiple patterns
    text_with_numbers = "Phone: 555-123-4567, Fax: 555-987-6543"
    new_text = re.sub(r"\d{3}-\d{3}-\d{4}", "XXX-XXX-XXXX", text_with_numbers)
    print(f"4. Masking phone numbers: \n   {new_text}")

if __name__ == "__main__":
    main()
