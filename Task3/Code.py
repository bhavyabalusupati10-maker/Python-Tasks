def main():
    print("=== Tuple-Based Transaction Audit ===")
    
    n = int(input("Enter number of transactions: "))
    
    transactions = []
    print("\nEnter transactions as ID Amount Type (e.g., T101 5000 credit):")
    for i in range(n):
        data = input(f"Transaction {i+1}: ").split()
        tid = data[0]
        amount = float(data[1])
        ttype = data[2].lower()
        transactions.append((tid, amount, ttype))
    
    seen_ids = []
    duplicate_ids = []
    invalid_amounts = []
    suspicious_list = []
    
    for tid, amount, ttype in transactions:
        if tid in seen_ids:
            if tid not in duplicate_ids:
                duplicate_ids.append(tid)
        else:
            seen_ids.append(tid)
        
        if amount <= 0:
            invalid_amounts.append((tid, amount, ttype))
        
        if amount > 100000:
            suspicious_list.append((tid, amount, ttype, "High Value"))
    
    count_map = {}
    for tid, _, _ in transactions:
        count_map[tid] = count_map.get(tid, 0) + 1
        if count_map[tid] > 3:
            suspicious_list.append((tid, 0, "", "Repeated ID >3 times"))
    
    print("\n========== AUDIT REPORT ==========")
    print(f"Total Transactions: {n}")
    
    print("\n--- Duplicate Identifiers ---")
    if duplicate_ids:
        print(f"Duplicates Found: {duplicate_ids}")
    else:
        print("No Duplicate IDs")
    
    print("\n--- Invalid Amounts ---")
    if invalid_amounts:
        for t in invalid_amounts:
            print(f"Invalid: {t}")
    else:
        print("No Invalid Amounts")
    
    print("\n--- Suspicious Sequences ---")
    if suspicious_list:
        for t in suspicious_list:
            print(f"Suspicious: {t}")
    else:
        print("No Suspicious Transactions")
    
    print("\n=== Audit Complete ===")

main()
