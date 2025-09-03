import re
from collections import namedtuple

def main():
    """
    Examples of extracting multiple matches.
    """
    print("=== Extracting Multiple Matches ===\n")
    
    # Sample text - Shopping cart
    text = """
    Order #: 987654
    Date: 06/01/2023
    
    Items:
    1. Laptop, Brand: TechPro, Model: X5, Price: $1,599.00
    2. Headphones, Brand: AudioMax, Model: WH-1000, Price: $249.50
    3. Keyboard, Brand: GameMaster, Model: K101, Price: $89.90
    
    Total: $1,938.40
    """
    print(f"Sample text: \n{text}")
    
    # Extract all products
    product_pattern = r"(\d+)\.\s(.+?),\sBrand:\s(.+?),\sModel:\s(.+?),\sPrice:\s\$([\d.,]+)"
    product_matches = re.findall(product_pattern, text)
    
    print("Product List:")
    for match in product_matches:
        item_no, product, brand, model, price = match
        print(f"  {item_no}. {product} ({brand} {model}) - ${price}")
    
    # Using named tuple for more organized output
    print("\nProduct List with Named Tuple:")
    Product = namedtuple('Product', ['item_no', 'name', 'brand', 'model', 'price'])
    
    products = [Product(*match) for match in product_matches]
    for product in products:
        print(f"  {product.item_no}. {product.name} ({product.brand} {product.model}) - ${product.price}")
    
    # Another example with findall
    print("\n=== Finding All Email Addresses ===\n")
    
    text_with_emails = """
    Contact us at support@example.com for general inquiries.
    For sales, email sales@example.com or call 555-123-4567.
    Technical support is available at tech.support@example.co.uk.
    """
    print(f"Text with emails:\n{text_with_emails}")
    
    email_pattern = r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+"
    emails = re.findall(email_pattern, text_with_emails)
    
    print("Found emails:")
    for i, email in enumerate(emails, 1):
        print(f"  {i}. {email}")

if __name__ == "__main__":
    main()
