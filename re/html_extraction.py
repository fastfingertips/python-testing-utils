import re

def main():
    """
    Example of extracting data from HTML content.
    """
    print("=== Extracting Data from HTML ===\n")
    
    # Simple HTML content
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sample Product Page</title>
    </head>
    <body>
        <div class="product">
            <h1>Smartphone XYZ</h1>
            <div class="price">$899.00</div>
            <div class="features">
                <ul>
                    <li>6.7 inch AMOLED Display</li>
                    <li>128GB Storage</li>
                    <li>8GB RAM</li>
                    <li>48MP Camera</li>
                </ul>
            </div>
            <div class="rating">4.7/5.0</div>
        </div>
        <div class="product">
            <h1>Tablet ABC</h1>
            <div class="price">$549.00</div>
            <div class="features">
                <ul>
                    <li>10.2 inch IPS Display</li>
                    <li>64GB Storage</li>
                    <li>4GB RAM</li>
                    <li>12MP Camera</li>
                </ul>
            </div>
            <div class="rating">4.5/5.0</div>
        </div>
    </body>
    </html>
    """
    
    # Extract product titles
    title_pattern = r'<h1>(.+?)</h1>'
    titles = re.findall(title_pattern, html)
    print("Product Titles:")
    for title in titles:
        print(f"  - {title}")
    
    # Extract prices
    price_pattern = r'<div class="price">(.+?)</div>'
    prices = re.findall(price_pattern, html)
    print("\nProduct Prices:")
    for price in prices:
        print(f"  - {price}")
    
    # Extract features
    feature_pattern = r'<li>(.+?)</li>'
    features = re.findall(feature_pattern, html)
    print("\nAll Features:")
    for feature in features:
        print(f"  - {feature}")
    
    # Extract ratings
    rating_pattern = r'<div class="rating">(.+?)</div>'
    ratings = re.findall(rating_pattern, html)
    print("\nProduct Ratings:")
    for rating in ratings:
        print(f"  - {rating}")
    
    # Extract product information as a whole
    print("\nExtract complete product information:")
    product_pattern = r'<div class="product">\s*<h1>(.+?)</h1>\s*<div class="price">(.+?)</div>'
    product_matches = re.findall(product_pattern, html, re.DOTALL)
    
    for i, (title, price) in enumerate(product_matches, 1):
        print(f"  Product {i}:")
        print(f"    Title: {title}")
        print(f"    Price: {price}")
    
    # Note about HTML parsing
    print("\nNote: For real HTML parsing, libraries like BeautifulSoup are more appropriate.")

if __name__ == "__main__":
    main()
