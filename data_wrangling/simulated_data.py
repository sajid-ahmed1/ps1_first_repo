import pandas as pd
import numpy as np

# create dataframe with 5 columns
data = {
    "household_id": [45, 45, 45, 245, 245, 600, 155800, 155800],
    "person": [1,2,3,1,2,1,1,2],
    "age": np.random.randint(1, 101, 8),
    "income": np.random.randint(500, 100001, 8),
    #To copy the lecture 2 table exactly, I imported numpy into my venv and added np.nan
    "female": [False, False, False, True, False, False, True, True]
}

df = pd.DataFrame(data)

print(df)

#To view this simulated data, run python3.12 simualted_data.py
#This runs the python software then the script and outputs the table in the terminal window