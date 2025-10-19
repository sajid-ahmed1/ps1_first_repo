import pandas as pd

def generate_household_level_date(df: pd.DataFrame):
    """
    Generate aggregated household-level data from individual-level data. For example, combing the individuals in house 1 to one unique row of house 1.
    Args:
        df (pandas.DataFrame): Individual-level data with columns 'household_id', 'person', 'age, 'income', and 'female'.
    Returns:
        pandas.DataFrame: Household-level data with aggregated statistics with columns 'household_id', 'household_size', 'mean_age', 'mean_income', 'num_female', and 'highest_earner_female'.
    """
    household_df = df.groupby('household_id').agg({
    'person': 'count','age': 'mean','income': 'mean','female': 'sum'
    })
    # Rename columns
    household_df.columns = ['household_size','mean_age','mean_income','num_female']

    # Reset the index to make household_id a column
    household_df = household_df.reset_index()
    #Apply that function during the groupby
    main_earner_female = (
        df.loc[df.groupby("household_id")["income"].idxmax(), ["household_id","female"]]
          .rename(columns={"female": "highest_earner_female"})
          .reset_index(drop=True)
    )

    household_df = household_df.merge(main_earner_female, on="household_id", how="left")
    print("Generated Household-Level Data:")
    return household_df
    
    

	
