import re

def main():
    """
    Simple regex pattern matching examples.
    """
    print("=== Simple Regex Pattern Matching Examples ===\n")
    
    # Sample text
    text = "Python programming language was created in 1991 by Guido van Rossum. Python 3.9 is one of the recent versions."
    print(f"Sample text: {text}\n")
    
    # 1. Simple word matching
    pattern = r"Python"
    matches = re.findall(pattern, text)
    print(f"1. Pattern '{pattern}' matches: {matches}")
    
    # 2. Number matching
    pattern = r"\d+"
    matches = re.findall(pattern, text)
    print(f"2. Pattern '{pattern}' matches (all numbers): {matches}")
    
    # 3. Word boundary matching
    pattern = r"\bPython\b"
    matches = re.findall(pattern, text)
    print(f"3. Pattern '{pattern}' matches (word boundaries): {matches}")

if __name__ == "__main__":
    main()
