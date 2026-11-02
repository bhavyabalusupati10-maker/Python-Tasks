def main():
    print("=== Water Distribution Fairness Analysis ===")
    
    areas = int(input("Enter number of areas: "))
    days = int(input("Enter number of days: "))
    
    print(f"\nEnter demand for {areas} areas:")
    demand = list(map(int, input().split()))
    
    print(f"\nEnter supply matrix {areas} x {days}:")
    supply = []
    for i in range(areas):
        row = list(map(int, input(f"Area {i+1} supply for {days} days: ").split()))
        supply.append(row)
    
    shortage = [[0]*days for _ in range(areas)]
    total_supply = [0]*areas
    total_shortage = [0]*areas
    
    for i in range(areas):
        for j in range(days):
            short = demand[i] - supply[i][j]
            if short < 0:
                short = 0
            shortage[i][j] = short
            total_supply[i] += supply[i][j]
            total_shortage[i] += short
    
    print("\n========== DISTRIBUTION REPORT ==========")
    print("\nSupply Matrix:")
    for i in range(areas):
        print(f"Area {i+1}: {supply[i]} -> Total {total_supply[i]}")
    
    print("\nShortage Matrix:")
    for i in range(areas):
        print(f"Area {i+1}: {shortage[i]} -> Total Shortage {total_shortage[i]}")
    
    print("\n--- Area-wise Analysis ---")
    for i in range(areas):
        avg_supply = total_supply[i] / days if days > 0 else 0
        fairness = (avg_supply / demand[i] * 100) if demand[i] > 0 else 0
        print(f"Area {i+1}: Demand {demand[i]}, Avg Supply {avg_supply:.2f}, Fairness {fairness:.2f}%, Total Shortage {total_shortage[i]}")
    
    max_shortage = max(total_shortage) if total_shortage else 0
    most_underserved = []
    for i in range(areas):
        if total_shortage[i] == max_shortage:
            most_underserved.append(f"Area {i+1}")
    
    print(f"\nMost Underserved Area(s): {', '.join(most_underserved)} with shortage {max_shortage}")
    
    if max_shortage == 0:
        print("Result: All Areas Fully Served")
    else:
        print("Result: Distribution Unfair - Underserved Areas Found")
    
    print("\n=== Analysis Complete ===")

main()
