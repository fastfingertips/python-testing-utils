import re

def main():
    """
    Demonstrates the difference between re.search() and re.match().
    """
    print("=== re.search() vs re.match() Comparison ===\n")
    
    text = "Python programming language is useful. Python can be used for web development."
    print(f"Sample text: {text}\n")
    
    # re.search() - finds pattern anywhere in the string
    search_result = re.search(r"web", text)
    if search_result:
        print(f"re.search(): '{search_result.group()}' found at position: {search_result.start()}-{search_result.end()}")
    else:
        print("re.search(): No match found")
    
    # re.match() - finds pattern only at the beginning of the string
    match_result = re.match(r"Python", text)
    if match_result:
        print(f"re.match(): '{match_result.group()}' found at position: {match_result.start()}-{match_result.end()}")
    else:
        print("re.match(): No match found")
    
    # re.match() with a pattern not at the beginning
    match_result = re.match(r"web", text)
    if match_result:
        print(f"re.match(): '{match_result.group()}' found at position: {match_result.start()}-{match_result.end()}")
    else:
        print("re.match(): No match found (because 'web' is not at the beginning)")
    
    # Additional example with re.fullmatch()
    fullmatch_result = re.fullmatch(r"Python.*development\.", text)
    if fullmatch_result:
        print(f"re.fullmatch(): Entire string matches the pattern")
    else:
        print("re.fullmatch(): String doesn't fully match the pattern")

if __name__ == "__main__":
    main()
