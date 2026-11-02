def main():
    print("=== Nested List Examination Seating Validation ===")
    
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    
    print(f"\nEnter seating matrix {r}x{c} (0=empty, -1=reserved, roll numbers):")
    seating = []
    for i in range(r):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        seating.append(row)
    
    print("\n========== SEATING MATRIX ==========")
    for row in seating:
        print(row)
    
    flat_list = []
    empty_seats = []
    reserved_seats = []
    invalid_alloc = []
    
    for i in range(r):
        for j in range(c):
            val = seating[i][j]
            if val == 0:
                empty_seats.append((i+1, j+1))
            elif val == -1:
                reserved_seats.append((i+1, j+1))
            elif val < -1:
                invalid_alloc.append((i+1, j+1, val))
            else:
                flat_list.append(val)
    
    duplicates = []
    seen = set()
    for roll in flat_list:
        if roll in seen and roll not in duplicates:
            duplicates.append(roll)
        seen.add(roll)
    
    print("\n========== VALIDATION REPORT ==========")
    print(f"Total Seats: {r*c}")
    print(f"Filled Seats: {len(flat_list)}")
    print(f"Empty Seats Count: {len(empty_seats)} -> {empty_seats}")
    print(f"Reserved Positions Count: {len(reserved_seats)} -> {reserved_seats}")
    print(f"Invalid Allocations Count: {len(invalid_alloc)} -> {invalid_alloc}")
    print(f"Duplicate Roll Numbers: {duplicates if duplicates else 'None'}")
    
    print("\n--- Final Validation ---")
    if duplicates:
        print(f"FAILED: Duplicate roll numbers found {duplicates}")
    else:
        print("PASSED: No duplicate roll numbers")
    
    if invalid_alloc:
        print(f"FAILED: Invalid student allocations found {invalid_alloc}")
    else:
        print("PASSED: No invalid allocations")
    
    if not duplicates and not invalid_alloc:
        print("\nOverall Result: SEATING MATRIX IS VALID")
    else:
        print("\nOverall Result: SEATING MATRIX IS INVALID")
    
    print("\n=== Validation Complete ===")

main()
