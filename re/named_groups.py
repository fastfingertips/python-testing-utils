import re

def main():
    """
    Data extraction examples using named groups.
    """
    print("=== Data Extraction with Named Groups ===\n")
    
    # Sample text
    text = """
    Product Information:
    Product Code: ABC-12345
    Product Name: Smartphone XYZ
    Price: $1,299.99
    Stock Status: Available (25 units)
    """
    print(f"Sample text: \n{text}")
    
    # Extract product information using named groups
    pattern = r"""
    Product\sCode:\s(?P<code>[A-Z]+-\d+).*?
    Product\sName:\s(?P<name>.+?).*?
    Price:\s(?P<price>\$[\d.,]+).*?
    Stock\sStatus:\s(?P<stock>.+)
    """
    
    match = re.search(pattern, text, re.DOTALL | re.VERBOSE)
    if match:
        print(f"Product Code: {match.group('code')}")
        print(f"Product Name: {match.group('name')}")
        print(f"Price: {match.group('price')}")
        print(f"Stock Status: {match.group('stock')}")
        
    # Another example with named groups
    print("\n=== Another Named Groups Example ===\n")
    
    # Parse a URL
    url = "https://www.example.com:8080/path/to/page.html?query=value&lang=en#section"
    
    url_pattern = r"""
    (?P<protocol>https?|ftp)://
    (?P<host>[\w.-]+)
    (?::(?P<port>\d+))?
    (?P<path>/[^\?#]*)?
    (?:\?(?P<query>[^#]*))?
    (?:#(?P<fragment>.*))?
    """
    
    url_match = re.search(url_pattern, url, re.VERBOSE)
    if url_match:
        print(f"URL: {url}")
        print(f"Protocol: {url_match.group('protocol')}")
        print(f"Host: {url_match.group('host')}")
        print(f"Port: {url_match.group('port')}")
        print(f"Path: {url_match.group('path')}")
        print(f"Query: {url_match.group('query')}")
        print(f"Fragment: {url_match.group('fragment')}")

if __name__ == "__main__":
    main()
