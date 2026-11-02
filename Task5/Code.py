def main():
    print("=== Smart Canteen Order and Stock Management ===")
    n = int(input("Enter number of items in inventory: "))
    inventory = {}
    print("\nEnter items as Name Qty Price (e.g., Samosa 50 15):")
    for i in range(n):
        data = input(f"Item {i+1}: ").split()
        name = data[0].lower()
        qty = int(data[1])
        price = float(data[2])
        inventory[name] = [qty, price]
    
    total_sales = 0
    sales_report = []
    
    while True:
        print("\n--- New Customer Order ---")
        item = input("Enter item name (or 'done' to close): ").lower()
        if item == 'done':
            break
        
        if item not in inventory:
            print(f"Rejected: {item} not available in inventory")
            continue
        
        req_qty = int(input(f"Enter quantity for {item}: "))
        available_qty = inventory[item][0]
        price = inventory[item][1]
        
        if req_qty > available_qty:
            print(f"Rejected: Only {available_qty} {item} available, requested {req_qty}")
            continue
        
        bill = req_qty * price
        inventory[item][0] -= req_qty
        total_sales += bill
        sales_report.append((item, req_qty, bill))
        print(f"Order Accepted: {item} x {req_qty} = Rs. {bill}")
        
        more = input("More orders from same customer? (yes/no): ").lower()
        if more != 'yes':
            print(f"Customer Bill Total processed")
    
    print("\n========== DAILY SUMMARY ==========")
    print(f"Total Sales: Rs. {total_sales}")
    print("\nSales Details:")
    for item, qty, bill in sales_report:
        print(f"{item} x {qty} = Rs. {bill}")
    
    print("\nRemaining Stock:")
    for item, (qty, price) in inventory.items():
        print(f"{item}: {qty} left @ Rs. {price}")
    
    print("\n=== Canteen Closed ===")

main()
