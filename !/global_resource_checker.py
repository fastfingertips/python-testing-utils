import socket
from urllib.parse import urlparse
import ipaddress

def verify_url(url):
    """
    Checks whether the given URL refers to a global resource.

    Args:
    url (str): The URL to be checked.

    Returns:
    bool: True if the URL refers to a global resource, False otherwise.
    """
    try:
        # Extract the domain name
        domain_name = urlparse(url).netloc

        # Perform a DNS query to obtain IP addresses
        host = socket.gethostbyname_ex(domain_name)

        # Check the obtained IP addresses
        for ip in host[2]:
            ip_addr = ipaddress.ip_address(ip)
            if not ip_addr.is_global:
                # Return False if at least one IP address is local
                return False
    except Exception:
        # Return False in case of an error
        return False

    # Return True if there is no error and the URL refers to a global resource
    return True

# Example usage
examples = [
    "https://www.google.com",
    "https://www.wikipedia.org",
    "https://www.youtube.com",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:8080/test",
    "http://127.0.0.1:8080/test",
    "https://www.google.com/test",
]

for url in examples:
    print(f"{url} refers to a global resource: {verify_url(url)}")