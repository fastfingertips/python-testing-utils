import re

def main():
    """
    Examples of re.compile() and regex flags.
    """
    print("=== re.compile() and Regex Flags ===\n")
    
    text = "Python programming language\nPYTHON is powerful.\npython can be used for data analysis."
    print(f"Sample text:\n{text}\n")
    
    # Normal compilation (case sensitive)
    pattern = re.compile(r"python")
    matches = pattern.findall(text)
    print(f"Normal compilation: {matches}")
    
    # Compilation with re.IGNORECASE flag
    pattern = re.compile(r"python", re.IGNORECASE)
    matches = pattern.findall(text)
    print(f"With IGNORECASE flag: {matches}")
    
    # Compilation with re.MULTILINE flag
    pattern = re.compile(r"^python", re.IGNORECASE | re.MULTILINE)
    matches = pattern.findall(text)
    print(f"With MULTILINE flag for line starts: {matches}")
    
    # Compilation with re.DOTALL flag
    text_with_newlines = "Start\nMiddle\nEnd"
    pattern = re.compile(r"Start.*End")
    matches = pattern.findall(text_with_newlines)
    print(f"Without DOTALL flag: {matches}")
    
    pattern = re.compile(r"Start.*End", re.DOTALL)
    matches = pattern.findall(text_with_newlines)
    print(f"With DOTALL flag: {matches}")

if __name__ == "__main__":
    main()
