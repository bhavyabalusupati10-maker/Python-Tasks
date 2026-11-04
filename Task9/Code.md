
Problem Statement: Nested List Examination Seating Validation

Validate a complete seating matrix for duplicate roll numbers, reserved positions, empty seats, and invalid student allocations.

Algorithm:
1. Start
2. Read rows and columns
3. Read seating matrix with roll numbers, 0 empty, -1 reserved
4. Initialize empty, reserved, invalid lists
5. Check duplicates in flat list
6. Scan each cell and categorize empty, reserved, invalid, valid
7. Count and display all categories
8. Validate no duplicates and no invalid allocations
9. Display final validation result
10. Stop

Flowchart:
```mermaid
flowchart TD
    A[Start] --> B[Read Rows Columns]
    B --> C[Read Seating Matrix]
    C --> D[Initialize Lists]
    D --> E[Check Duplicates in Flat List]
    E --> F[Scan Each Cell Position]
    F --> G{Value 0?}
    G -- Yes --> H[Empty Seat]
    G -- No --> I{Value -1?}
    I -- Yes --> J[Reserved Seat]
    I -- No --> K{Value > 0 and Valid?}
    K -- Yes --> L[Valid Student Allocation]
    K -- No --> M[Invalid Allocation]
    H --> N{More Cells?}
    J --> N
    L --> N
    M --> N
    N -- Yes --> F
    N -- No --> O[Count and Display All Categories]
    O --> P{No Duplicates and No Invalid?}
    P -- Yes --> Q[Validation Passed]
    P -- No --> R[Validation Failed]
    Q --> S[Stop]
    R --> S
```

Sample Input:
Enter rows: 2
