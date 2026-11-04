
Problem Statement: Hackathon Team Formation and Ranking System

Develop a system to validate hackathon teams and rank them fairly. Each team must have 2 to 4 members. For each valid team, calculate Total Score from 3 rounds (R1+R2+R3) and Average of individual scores.

Ranking Criteria (Tie Breakers): 
1. Higher Total Score
2. Higher Round 3 Score
3. Higher Average Score
4. Alphabetical Order of Team Name

Algorithm:
Step 1: Start
Step 2: Read number of teams n
Step 3: Initialize valid_teams as empty list
Step 4: For (i in range n, a)
Step 5: Read Team Name and Member Names
Step 6: Calculate team_size = len(members)
Step 7: If team_size < 2 or team_size > 4: Invalid and skip
Step 8: Read Individual Scores and Round Scores R1 R2 R3
Step 9: Calculate total = R1+R2+R3
Step 10: Calculate average = sum(ind_scores)/team_size
Step 11: Store team data in dictionary and append to valid_teams
Step 12: Sort valid_teams by key = (-total, -R3, -average, name)
Step 13: Display ranking table with Rank, Team Name, Total, R3, Avg, Size
Step 14: Stop

Flowchart:
```mermaid
flowchart TD
    A[Start] --> B[Read Number of Teams]
    B --> C[Initialize Valid Teams List]
    C --> D[Read Team Name and Members]
    D --> E[Calculate Team Size]
    E --> F{Is Size 2 to 4?}
    F -- No --> G[Print Invalid Skip Team]
    G --> J{More Teams?}
    F -- Yes --> H[Read Individual and Round Scores]
    H --> I[Calculate Total and Average]
    I --> K[Store Valid Team]
    K --> J
    J -- Yes --> D
    J -- No --> L[Sort Teams]
    L --> M[Display Ranking]
    M --> N[Stop]
