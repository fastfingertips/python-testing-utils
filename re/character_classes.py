import re

def main():
    """
    Examples of character classes in regex.
    """
    print("=== Character Classes in Regex ===\n")
    
    # Sample text
    text = "Python programming language was created in 1991 by Guido van Rossum. Python 3.9 is one of the recent versions."
    print(f"Sample text: {text}\n")
    
    # 1. Digit character class
    pattern = r"[0-9]+"
    matches = re.findall(pattern, text)
    print(f"1. Pattern '{pattern}' matches (digit sequences): {matches}")
    
    # 2. Word character class
    pattern = r"[a-zA-Z]+"
    matches = re.findall(pattern, text)
    print(f"2. Pattern '{pattern}' matches (word sequences): {matches}")
    
    # 3. Custom character class
    pattern = r"[Ppy]"
    matches = re.findall(pattern, text)
    print(f"3. Pattern '{pattern}' matches (P, p, or y): {matches}")
    
    # 4. Negated character class
    pattern = r"[^a-z ]+"
    matches = re.findall(pattern, text)
    print(f"4. Pattern '{pattern}' matches (not lowercase or space): {matches}")

if __name__ == "__main__":
    main()
