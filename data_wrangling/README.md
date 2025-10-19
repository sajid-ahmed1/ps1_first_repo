## Objective

Reconstruct the simulated data frame from Lecture 2, then perform the necessary data wrangling to transform the individual-level data frame into a household-level data frame.

![Household Level.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/00734747-c571-451a-a8a2-d159b4c32747/bec3039f-b09d-49b4-ae45-db5147f0b737/Household_Level.png)

## Tasks

1. Recreate the initial data frame as shown in the provided screenshot. Use simulated data to generate a new data frame containing the specified information.
2. Develop functions to derive the features displayed in the household-level data frame (the second screenshot).
3. Adhere to Git and GitHub workflow practices:
    - Create a separate branch for each new function
    - Submit a Pull Request (PR) for each function
    - Merge the PR into the main branch upon completion
4. You may complete this assignment individually or in teams.

## Guidelines:

1. Utilise Git and GitHub
2. Implement a modular code structure to enhance maintainability:
    - Create functions within separate modules
    - Import these functions into your main orchestration script
        - Use the imported functions to execute the steps "create_simulated_data()" and "generate_household_level_data()" (you are free to come up with better naming)

## Reflection Question

**Question**: What are some potential use cases for generating simulated data?
**Answer**: Some potential use cases:
1. Sampling a dataset for practise or testing code
2. Stress testing performance
3. Confidence in the ETL process
4. Build edge cases that could be one-off or sporadically occuring
5. Synthetic datasets - when you cannot use protected data (C3/C4 Classified data) so using the same schema but random numbers to build a prototype