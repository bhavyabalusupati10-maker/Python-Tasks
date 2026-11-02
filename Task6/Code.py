def main():
    print("=== Library Borrowing and Fine Reconciliation ===")
    n = int(input("Enter number of borrowing records: "))
    
    records = []
    print("\nEnter records as BookID Period Delay (e.g., B101 14 3):")
    for i in range(n):
        data = input(f"Record {i+1}: ").split()
        book_id = data[0]
        period = int(data[1])
        delay = int(data[2])
        records.append((book_id, period, delay))
    
    fine_rate = int(input("\nEnter fine per day: "))
    
    total_fine = 0
    overdue_records = []
    available_books = []
    all_books = {}
    
    for book_id, period, delay in records:
        all_books[book_id] = True
        
        if delay > 0:
            fine = delay * fine_rate
            total_fine += fine
            overdue_records.append((book_id, period, delay, fine))
        else:
            available_books.append(book_id)
    
    print("\n========== RECONCILIATION REPORT ==========")
    print(f"Total Records: {n}")
    
    print("\n--- Overdue Records ---")
    if overdue_records:
        for book_id, period, delay, fine in overdue_records:
            print(f"Book {book_id}: Period {period} days, Delay {delay} days -> Fine Rs. {fine}")
    else:
        print("No Overdue Records")
    
    print(f"\nTotal Fine Collected: Rs. {total_fine}")
    
    print("\n--- Book Availability ---")
    print(f"Books Returned On Time: {available_books}")
    print(f"Total Books Reconciled: {len(all_books)} Available")
    
    print("\n=== Library Reconciliation Complete ===")

main()
