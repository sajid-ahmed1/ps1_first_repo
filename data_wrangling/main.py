from generate_household_level_data import generate_household_level_date
import simulated_data

"""
Main orchestration script.

Steps:
1. Generate simulated person-level data from simulated_data.py.
2. Aggregate to household-level features using the imported function generate_household_level_date.
3. Print outputs.
"""

def main():
    """
    Orchestrates data simulation and household-level aggregation.
    """
    # Generate household-level data from individual-level data
    household_data = generate_household_level_date(simulated_data.df)
    print(household_data)

    
if __name__ == "__main__":
    main()