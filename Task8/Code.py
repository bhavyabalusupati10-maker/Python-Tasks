def main():
    print("=== Manufacturing Quality Control Matrix ===")
    
    p = int(input("Enter number of products: "))
    b = int(input("Enter number of batches: "))
    
    print(f"\nEnter Production Matrix ({p} products x {b} batches):")
    production = []
    for i in range(p):
        row = list(map(int, input(f"Product {i+1} production quantities: ").split()))
        production.append(row)
    
    print(f"\nEnter Defective Matrix ({p} products x {b} batches):")
    defective = []
    for i in range(p):
        row = list(map(int, input(f"Product {i+1} defective units: ").split()))
        defective.append(row)
    
    threshold = float(input("\nEnter quality threshold %: "))
    
    defect_percent = [[0.0 for _ in range(b)] for _ in range(p)]
    flagged = []
    
    total_prod = 0
    total_def = 0
    
    for i in range(p):
        for j in range(b):
            prod = production[i][j]
            defe = defective[i][j]
            total_prod += prod
            total_def += defe
            if prod > 0:
                perc = (defe / prod) * 100
            else:
                perc = 0.0
            defect_percent[i][j] = perc
            if perc > threshold:
                flagged.append((i+1, j+1, perc))
    
    print("\n========== QUALITY CONTROL REPORT ==========")
    print("\nProduction Matrix:")
    for i in range(p):
        print(f"Product {i+1}: {production[i]}")
    
    print("\nDefective Matrix:")
    for i in range(p):
        print(f"Product {i+1}: {defective[i]}")
    
    print("\nDefect Percentage Matrix (%):")
    for i in range(p):
        formatted = [f"{x:.2f}%" for x in defect_percent[i]]
        print(f"Product {i+1}: {formatted}")
    
    print(f"\nQuality Threshold: {threshold}%")
    print("\n--- Batches Exceeding Threshold ---")
    if flagged:
        for prod_no, batch_no, perc in flagged:
            print(f"Product {prod_no} Batch {batch_no}: {perc:.2f}% - FAILED")
    else:
        print("All Batches Passed Quality Check")
    
    overall = (total_def / total_prod * 100) if total_prod > 0 else 0
    print(f"\nTotal Production: {total_prod}")
    print(f"Total Defective: {total_def}")
    print(f"Overall Defect %: {overall:.2f}%")
    
    print("\n=== Quality Control Complete ===")

main()
