import pandas as pd


import pandas as pd
import os

current_dir = os.path.dirname(__file__)

file_path = os.path.join(current_dir, 'data.csv')

# Check if the file exists
if os.path.exists(file_path):
    try:
        df = pd.read_csv(file_path)

        new_df = df.dropna()
        #Note: By default, the dropna() method returns a new DataFrame, and will not change the original.
        #Return a new Data Frame with no empty cells:
        print(new_df.to_string())

        df.dropna(inplace = True)
        #If you want to change the original DataFrame, use the inplace = True argument:
        #Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, 
        # but it will remove all rows containing NULL values from the original DataFrame.
        print(df.to_string())
        df.fillna(130, inplace = True)
        print(df.to_string())

        df["Calories"].fillna(130, inplace = True)
        x = df["Calories"].mean()
        #A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

        #Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:
        #Mean = the average value (the sum of all values divided by number of values).
        df["Calories"].fillna(x, inplace = True)
        x = df["Calories"].median()
        #Median = the value in the middle, after you have sorted all values ascending.
        df["Calories"].fillna(x, inplace = True)

        x = df["Calories"].mode()[0]

        df["Calories"].fillna(x, inplace = True)
        #Mode = the value that appears most frequently.

    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
else:
    print(f"The file {file_path} does not exist.")

