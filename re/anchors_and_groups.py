import re

def main():
    """
    Examples of anchors and groups in regex.
    """
    print("=== Anchors and Groups in Regex ===\n")
    
    # Sample text
    text = "Python programming language was created in 1991 by Guido van Rossum. Python 3.9 is one of the recent versions."
    print(f"Sample text: {text}\n")
    
    # 1. Start anchor
    pattern = r"^Python"
    matches = re.findall(pattern, text)
    print(f"1. Pattern '{pattern}' matches (Python at start): {matches}")
    
    # 2. End anchor
    pattern = r"versions\.$"
    matches = re.findall(pattern, text)
    print(f"2. Pattern '{pattern}' matches (versions. at end): {matches}")
    
    # 3. Simple capturing group
    pattern = r"Python (\d+\.\d+)"
    matches = re.findall(pattern, text)
    print(f"3. Pattern '{pattern}' matches (Python version numbers): {matches}")
    
    # 4. Multiple capturing groups
    pattern = r"in (\d+) by ([A-Za-z ]+)"
    matches = re.findall(pattern, text)
    print(f"4. Pattern '{pattern}' matches (year and creator): {matches}")
    
    # 5. Named capturing groups
    pattern = r"Python (?P<version>\d+\.\d+)"
    matches = re.search(pattern, text)
    if matches:
        print(f"5. Named group 'version': {matches.group('version')}")

if __name__ == "__main__":
    main()
