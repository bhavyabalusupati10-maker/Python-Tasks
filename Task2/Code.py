def main():
    print("=== Multi-Branch Expense Matrix Analysis ===")
    
    B = int(input("Enter number of branches (B): "))
    C = int(input("Enter number of categories (C): "))
    
    print(f"\nEnter expense matrix {B} x {C}:")
    expenses = []
    for i in range(B):
        row = list(map(int, input(f"Branch {i+1} ({C} values): ").split()))
        expenses.append(row)
    
    branch_totals = []
    category_totals = [0] * C
    
    for i in range(B):
        branch_totals.append(sum(expenses[i]))
        for j in range(C):
            category_totals[j] += expenses[i][j]
    
    overall_total = sum(branch_totals)
    overall_average = overall_total / (B * C) if B*C != 0 else 0
    
    branch_averages = [t / C for t in branch_totals]
    category_averages = [t / B for t in category_totals]
    
    max_branch = max(branch_totals)
    max_branch_idx = branch_totals.index(max_branch)
    
    max_category = max(category_totals)
    max_category_idx = category_totals.index(max_category)
    
    print("\n========== RESULTS ==========")
    for i in range(B):
        print(f"Branch {i+1}: {expenses[i]} -> Total: {branch_totals[i]}, Avg: {branch_averages[i]:.2f}")
    
    print(f"\nCategory Totals: {category_totals}")
    print(f"Category Averages: {[round(x,2) for x in category_averages]}")
    print(f"\nOverall Total: {overall_total}")
    print(f"Overall Average: {overall_average:.2f}")
    
    print(f"\n--- Largest Contributors ---")
    print(f"Highest Branch: Branch {max_branch_idx+1} with {max_branch}")
    print(f"Highest Category: Category {max_category_idx+1} with {max_category}")

main()
