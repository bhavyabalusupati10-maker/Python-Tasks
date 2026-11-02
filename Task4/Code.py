def main():
    print("=== Student Group Formation with Score Balancing ===")
    
    n = int(input("Enter number of students: "))
    scores = list(map(int, input(f"Enter {n} scores: ").split()))
    
    g = int(input("Enter number of groups: "))
    group_sizes = list(map(int, input(f"Enter {g} group sizes: ").split()))
    
    sorted_scores = sorted(scores, reverse=True)
    
    groups = [[] for _ in range(g)]
    group_totals = [0] * g
    group_counts = [0] * g
    
    for score in sorted_scores:
        min_total = float('inf')
        min_index = -1
        for i in range(g):
            if group_counts[i] < group_sizes[i]:
                if group_totals[i] < min_total:
                    min_total = group_totals[i]
                    min_index = i
        if min_index != -1:
            groups[min_index].append(score)
            group_totals[min_index] += score
            group_counts[min_index] += 1
    
    print("\n========== GROUP ALLOCATION ==========")
    for i in range(g):
        print(f"Group {i+1}: {groups[i]} -> Total: {group_totals[i]}")
    
