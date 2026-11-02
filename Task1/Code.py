

def get_valid_teams():
    valid_teams = []
    
    n = int(input("Enter number of teams: "))
    
    for i in range(n):
        print(f"\n--- Team {i+1} ---")
        team_name = input("Enter Team Name: ")
        
        members_input = input("Enter Member Names (comma separated): ")
        members = [m.strip() for m in members_input.split(',') if m.strip()]
        team_size = len(members)
        
        # Step 4 & 5: Validate Team Size
        if team_size < 2 or team_size > 4:
            print(f"Invalid Team '{team_name}': Team size {team_size} is not between 2 and 4. Skipping.")
            # Still need to consume score inputs to keep flow
            try:
                input("Enter Individual Scores (comma separated) [skipped]: ")
                input("Enter Round Scores R1 R2 R3 (space separated) [skipped]: ")
            except:
                pass
            continue
        
        scores_input = input(f"Enter Individual Scores for {team_size} members (comma separated): ")
        ind_scores = list(map(int, scores_input.split(',')))
        
        round_input = input("Enter Round1 Round2 Round3 scores (space separated): ")
        r1, r2, r3 = map(int, round_input.split())
        
        # Step 6 & 7: Calculate scores
        total_score = r1 + r2 + r3
        avg_score = sum(ind_scores) / team_size if team_size > 0 else 0
        
        team_data = {
            'name': team_name,
            'members': members,
            'size': team_size,
            'ind_scores': ind_scores,
            'r1': r1,
            'r2': r2,
            'r3': r3,
            'total': total_score,
            'average': avg_score
        }
        valid_teams.append(team_data)
    
    return valid_teams

def rank_teams(teams):
    # Step 9 & 10: Sort with Tie Breakers
    # Sort by: Total DESC, Round3 DESC, Average DESC, Name ASC
    sorted_teams = sorted(teams, key=lambda x: (-x['total'], -x['r3'], -x['average'], x['name']))
    return sorted_teams

def display_ranking(teams):
    print("\n========== FINAL HACKATHON RANKING ==========")
    if not teams:
        print("No valid teams to rank.")
        return
        
    print(f"{'Rank':<5} {'Team Name':<15} {'Total':<7} {'R3':<5} {'Avg':<7} {'Size'}")
    print("-" * 55)
    for rank, team in enumerate(teams, 1):
        print(f"{rank:<5} {team['name']:<15} {team['total']:<7} {team['r3']:<5} {team['average']:<7.2f} {team['size']}")
print("Hackathon Team Formation and Ranking")
valid_list = get_valid_teams()
ranked_list = rank_teams(valid_list)
display_ranking(ranked_list)
