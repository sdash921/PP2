import re
import json

def parse_receipt(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # 1. Extract Date and Time
    # Pattern: DD/MM/YYYY and HH:MM
    date = re.search(r'(\d{2}/\d{2}/\d{4})', content)
    time = re.search(r'(\d{2}:\d{2})', content)

    # 2. Extract Product Names and Prices
    # Pattern: Captures text after 'x ' and before '...' 
    # and captures the price after the '$'
    products = []
    # Find all lines like "1x PRODUCT NAME ... $0.00"
    items = re.findall(r'\d+x\s+(.*?)\s+\.*\$(\d+\.\d{2})', content)
    
    for name, price in items:
        products.append({
            "name": name.strip(),
            "price": float(price)
        })

    # 3. Extract Total Amount
    # Pattern: Looks for 'TOTAL AMOUNT:' followed by '$' and digits
    total_match = re.search(r'TOTAL AMOUNT:\s*\$(\d+\.\d{2})', content)
    total_amount = float(total_match.group(1)) if total_match else 0.0

    # 4. Extract Payment Method
    # Pattern: Everything after 'PAYMENT METHOD: '
    payment_match = re.search(r'PAYMENT METHOD:\s*(.*)', content)
    payment_method = payment_match.group(1).strip() if payment_match else "Unknown"

    # Create Structured Output
    receipt_data = {
        "metadata": {
            "date": date.group(1) if date else None,
            "time": time.group(1) if time else None
        },
        "items": products,
        "total": total_amount,
        "payment_method": payment_method
    }

    return receipt_data

if __name__ == "__main__":
    data = parse_receipt('raw.txt')
    
    # Print formatted text
    print("--- PARSED RECEIPT DATA ---")
    print(f"Date: {data['metadata']['date']} | Time: {data['metadata']['time']}")
    print("-" * 30)
    for item in data['items']:
        print(f"- {item['name']}: ${item['price']}")
    print("-" * 30)
    print(f"TOTAL: ${data['total']}")
    print(f"Payment: {data['payment_method']}")
    
    # Save as JSON for GitHub structure
    with open('parsed_receipt.json', 'w') as f:
        json.dump(data, f, indent=4)