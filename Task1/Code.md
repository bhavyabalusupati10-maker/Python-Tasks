Problem Statement:
52. Hackathon Team Formation and Ranking: Analyse student scores and team compositions, validate team sizes, aggregate round scores and rank teams.

Algorithm:
Step 1: Start
Step 2: Read number of teams
Step 3: For each team, read Team Name, Members, Individual Scores, Round1, Round2, Round3
Step 4: Validate Team Size
Step 5: If Size < 2 or Size > 4 Then Invalid Team, go to next team
Step 6: Calculate Total Score = Round1 + Round2 + Round3
Step 7: Calculate Average Score = Sum of Individual Scores / Team Size
Step 8: Store valid teams in list
Step 9: Sort list by Total Score Descending
Step 10: If Tie, apply rules: Higher Round 3, Higher Average, Alphabetical Name
Step 11: Assign ranks and display result
Step 12: Stop

Flowchart:
```mermaid
flowchart TD
    First([Start]) --> A[Read Number of Teams]
    A --> B[Input Team Details]
    B --> C{Is Team Size >=2 and <=4?}
    C -- No --> D[Invalid Team] --> E{More Teams?}
    C -- Yes --> F[Total = R1+R2+R3]
    F --> G[Average = Sum / Size]
    G --> H[Store Team Data]
    H --> E
    E -- Yes --> B
    E -- No --> I[Sort by Total Score]
    I --> J{Check Tie?}
    J -- Yes --> K[Apply Tie Breaker]
    J -- No --> L[Assign Rank]
    K --> L
    L --> M[Display Final Ranking]
    M --> Last([Stop])
```
